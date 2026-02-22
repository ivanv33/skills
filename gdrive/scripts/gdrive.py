# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "google-api-python-client",
#     "google-auth",
# ]
# ///

import argparse
import io
import logging
import os
import re
import sys
from urllib.parse import parse_qs, urlparse

import google.auth
import google.auth.transport.requests
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

log = logging.getLogger(__name__)

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


FORMAT_MAPPING = {
    "md": "text/markdown",
    "markdown": "text/markdown",
    "txt": "text/plain",
    "text": "text/plain",
    "pdf": "application/pdf",
    "rtf": "application/rtf",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "html": "text/html",
    "epub": "application/epub+zip",
}

WEB_EXPORT_FORMATS = {
    "md": "markdown",
    "markdown": "markdown",
    "txt": "txt",
    "text": "txt",
    "pdf": "pdf",
    "rtf": "rtf",
    "docx": "docx",
    "html": "html",
    "epub": "epub",
}

_DOC_ID_RE = re.compile(r"/document/d/([a-zA-Z0-9_-]+)")


def parse_doc_input(raw):
    """Parse a doc ID or Google Docs URL into (doc_id, tab_id | None)."""
    if "://" not in raw:
        return raw, None

    parsed = urlparse(raw)
    if parsed.hostname not in ("docs.google.com", "www.docs.google.com"):
        raise ValueError(f"Not a Google Docs URL: {raw}")

    match = _DOC_ID_RE.search(parsed.path)
    if not match:
        raise ValueError(f"Could not extract document ID from URL: {raw}")

    doc_id = match.group(1)
    qs = parse_qs(parsed.query)
    tab_id = qs.get("tab", [None])[0]
    return doc_id, tab_id


def _export_default(service, doc_id, mime_type):
    """Export via Drive API (no tab support)."""
    request = service.files().export_media(fileId=doc_id, mimeType=mime_type)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            log.debug("Download %d%%.", int(status.progress() * 100))
    return buf.getvalue()


def _export_tab(doc_id, tab_id, export_format):
    """Export a specific tab via authenticated web export endpoint."""
    creds, _ = google.auth.default(scopes=SCOPES)
    session = google.auth.transport.requests.AuthorizedSession(creds)

    fmt = WEB_EXPORT_FORMATS.get(export_format)
    url = f"https://docs.google.com/document/export?format={fmt}&id={doc_id}&tab={tab_id}"
    resp = session.get(url)

    if resp.status_code == 200:
        return resp.content

    # Markdown may not be supported via web export; fall back to txt
    if fmt == "markdown":
        log.warning("Web export does not support markdown for tabs; falling back to txt.")
        url = f"https://docs.google.com/document/export?format=txt&id={doc_id}&tab={tab_id}"
        resp = session.get(url)
        if resp.status_code == 200:
            return resp.content

    log.error("Tab export failed (HTTP %d): %s", resp.status_code, resp.text[:200])
    sys.exit(1)


def get_drive_service():
    try:
        creds, _ = google.auth.default(scopes=SCOPES)
    except google.auth.exceptions.DefaultCredentialsError:
        log.error("Credentials not found. Set GOOGLE_APPLICATION_CREDENTIALS or run gcloud auth application-default login.")
        sys.exit(1)

    if creds.expired and creds.refresh_token:
        creds.refresh(google.auth.transport.requests.Request())

    return build("drive", "v3", credentials=creds, cache_discovery=False)


def cmd_get(service, args):
    doc_id, tab_id = parse_doc_input(args.doc_id)
    output_filename = args.output
    export_format = args.format

    # Guess format from output extension if format is default
    if export_format == "md" and output_filename:
        _, ext = os.path.splitext(output_filename)
        if ext:
            guess_ext = ext.lstrip(".").lower()
            if guess_ext in FORMAT_MAPPING:
                export_format = guess_ext

    mime_type = FORMAT_MAPPING.get(export_format.lower())
    if not mime_type:
        log.error("Unsupported format: %s. Supported: %s", export_format, ", ".join(FORMAT_MAPPING))
        sys.exit(1)

    should_log = output_filename is not None

    try:
        if should_log:
            log.info("Downloading to %s...", output_filename)

        if tab_id:
            content = _export_tab(doc_id, tab_id, export_format)
        else:
            content = _export_default(service, doc_id, mime_type)

        if output_filename:
            with open(output_filename, "wb") as f:
                f.write(content)
            log.info("Done.")
        else:
            sys.stdout.buffer.write(content)
            sys.stdout.flush()

    except SystemExit:
        raise
    except Exception as error:
        log.error("An error occurred: %s", error)
        sys.exit(1)


def cmd_query(service, args):
    try:
        q = f"name contains '{args.name}' and mimeType='application/vnd.google-apps.document' and trashed=false"
        if args.meta:
            fields = "nextPageToken, files(id, name, createdTime, modifiedTime, owners(emailAddress), permissions(emailAddress, role), webViewLink)"
        else:
            fields = "nextPageToken, files(id, name)"
        results = service.files().list(q=q, pageSize=10, fields=fields).execute()
        items = results.get("files", [])

        if not items:
            log.info("No files found.")
        elif args.meta:
            for item in items:
                owner = item.get("owners", [{}])[0].get("emailAddress", "unknown")
                shared = [
                    f"{p['emailAddress']} ({p['role']})"
                    for p in item.get("permissions", [])
                    if p.get("emailAddress") and p["emailAddress"] != owner
                ]
                print(f"{item['name']} ({item['id']})")
                print(f"  created: {item.get('createdTime', '?')}  modified: {item.get('modifiedTime', '?')}")
                print(f"  owner: {owner}")
                if shared:
                    print(f"  shared: {', '.join(shared)}")
                print(f"  link: {item.get('webViewLink', '?')}")
        else:
            for item in items:
                print(f"{item['name']} ({item['id']})")

    except Exception as error:
        log.error("An error occurred: %s", error)
        sys.exit(1)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="GDrive CLI tool for querying and exporting Google Docs")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.required = True

    parser_query = subparsers.add_parser("query", help="Search for Google Docs by name")
    parser_query.add_argument("name", help="Part of the file name to search for")
    parser_query.add_argument("--meta", action="store_true", help="Include metadata (modified time, owner, link)")

    parser_get = subparsers.add_parser("get", help="Export a Google Doc")
    parser_get.add_argument("doc_id", help="Document ID or full Google Docs URL (tab param supported)")
    parser_get.add_argument("-o", "--output", default=None, help="Output filename (default: stdout)")
    parser_get.add_argument("-f", "--format", default="md", choices=FORMAT_MAPPING.keys(), help="Export format (default: md)")

    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")

    service = get_drive_service()

    commands = {
        "query": cmd_query,
        "get": cmd_get,
    }
    commands[args.command](service, args)


if __name__ == "__main__":
    main()
