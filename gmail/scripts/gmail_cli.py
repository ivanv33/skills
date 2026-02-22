# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "google-api-python-client",
#     "google-auth",
# ]
# ///

import base64
import logging
import sys
from email.mime.text import MIMEText

import google.auth
import google.auth.transport.requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

log = logging.getLogger(__name__)

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def get_gmail_service():
    try:
        creds, _ = google.auth.default(scopes=SCOPES)
    except google.auth.exceptions.DefaultCredentialsError:
        log.error("Credentials not found. Set GOOGLE_APPLICATION_CREDENTIALS or run gcloud auth application-default login.")
        sys.exit(1)

    if creds.expired and creds.refresh_token:
        creds.refresh(google.auth.transport.requests.Request())

    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def get_header(msg, name):
    for h in msg.get("payload", {}).get("headers", []):
        if h["name"].lower() == name.lower():
            return h["value"]
    return None


def build_mime_message(
    to, subject, body, from_addr="me", cc=None, bcc=None,
    in_reply_to=None, references=None,
):
    msg = MIMEText(body, "plain", "utf-8")
    msg["To"] = to
    msg["From"] = from_addr
    msg["Subject"] = subject
    if cc:
        msg["Cc"] = cc
    if bcc:
        msg["Bcc"] = bcc
    if in_reply_to:
        msg["In-Reply-To"] = in_reply_to
    if references:
        msg["References"] = references
    return base64.urlsafe_b64encode(msg.as_bytes()).decode("ascii")


def read_body(body_arg):
    if body_arg == "-":
        return sys.stdin.read()
    return body_arg


def _format_messages(service, message_ids, fmt):
    if not message_ids:
        print("No messages found.")
        return

    api_format = "full" if fmt == "full" else "metadata"
    metadata_headers = ["From", "To", "Subject", "Date"]

    for msg_ref in message_ids:
        kwargs = {"userId": "me", "id": msg_ref["id"], "format": api_format}
        if api_format == "metadata":
            kwargs["metadataHeaders"] = metadata_headers
        msg = service.users().messages().get(**kwargs).execute()

        if fmt == "full":
            subject = get_header(msg, "Subject") or "(no subject)"
            from_addr = get_header(msg, "From") or ""
            date = get_header(msg, "Date") or ""
            body_text = _extract_body(msg)
            print(f"--- {msg['id']} | {date} | {from_addr} ---")
            print(f"Subject: {subject}")
            print(body_text)
            print()
        else:
            mid = msg["id"]
            date = get_header(msg, "Date") or ""
            from_addr = get_header(msg, "From") or ""
            subject = get_header(msg, "Subject") or "(no subject)"
            snippet = msg.get("snippet", "")
            print(f"{mid}  {date}  {from_addr}  {subject}  {snippet}")


def _extract_body(msg):
    payload = msg.get("payload", {})
    # Try top-level body
    data = payload.get("body", {}).get("data")
    if data:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
    # Try multipart — prefer text/plain
    for part in payload.get("parts", []):
        if part.get("mimeType") == "text/plain":
            data = part.get("body", {}).get("data")
            if data:
                return base64.urlsafe_b64decode(data).decode(
                    "utf-8", errors="replace"
                )
    return "(no body)"


def cmd_inbox(service, args):
    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX"],
        maxResults=args.max_results,
    ).execute()
    _format_messages(service, results.get("messages", []), args.format)


def cmd_search(service, args):
    results = service.users().messages().list(
        userId="me",
        q=args.query,
        maxResults=args.max_results,
    ).execute()
    _format_messages(service, results.get("messages", []), args.format)


def cmd_send(service, args):
    body = read_body(args.body)
    raw = build_mime_message(
        to=args.to,
        subject=args.subject,
        body=body,
        from_addr=args.from_addr,
        cc=args.cc,
        bcc=args.bcc,
    )
    try:
        result = service.users().messages().send(
            userId="me", body={"raw": raw}
        ).execute()
        log.info("Sent: %s", result["id"])
    except HttpError as e:
        log.error("Failed to send: %s", e)
        sys.exit(1)


def cmd_reply(service, args):
    try:
        original = service.users().messages().get(
            userId="me", id=args.message_id, format="metadata",
            metadataHeaders=["From", "To", "Cc", "Subject", "Message-ID"],
        ).execute()
    except HttpError as e:
        log.error("Message not found: %s", e)
        sys.exit(1)

    thread_id = original["threadId"]
    subject = get_header(original, "Subject") or ""
    if not subject.lower().startswith("re:"):
        subject = f"Re: {subject}"

    reply_to = get_header(original, "From") or ""
    original_message_id = get_header(original, "Message-ID")

    cc = args.cc
    if args.reply_all:
        original_to = get_header(original, "To") or ""
        original_cc = get_header(original, "Cc") or ""
        all_recipients = [
            a.strip()
            for a in (original_to + "," + original_cc).split(",")
            if a.strip()
        ]
        extra = ",".join(all_recipients) if all_recipients else None
        if cc and extra:
            cc = f"{cc},{extra}"
        elif extra:
            cc = extra

    body = read_body(args.body)
    raw = build_mime_message(
        to=reply_to,
        subject=subject,
        body=body,
        cc=cc,
        in_reply_to=original_message_id,
        references=original_message_id,
    )
    try:
        result = service.users().messages().send(
            userId="me", body={"raw": raw, "threadId": thread_id}
        ).execute()
        log.info("Reply sent: %s", result["id"])
    except HttpError as e:
        log.error("Failed to reply: %s", e)
        sys.exit(1)


def parse_args(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description="Gmail CLI")
    parser.add_argument("-v", "--verbose", action="store_true")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    # inbox
    p_inbox = subparsers.add_parser("inbox", help="List recent inbox messages")
    p_inbox.add_argument("-n", "--max-results", type=int, default=10)
    p_inbox.add_argument(
        "-f", "--format", choices=["summary", "full"], default="summary"
    )

    # search
    p_search = subparsers.add_parser("search", help="Search all mail")
    p_search.add_argument("query", help="Gmail search query")
    p_search.add_argument("-n", "--max-results", type=int, default=10)
    p_search.add_argument(
        "-f", "--format", choices=["summary", "full"], default="summary"
    )

    # send
    p_send = subparsers.add_parser("send", help="Send an email")
    p_send.add_argument("--to", required=True)
    p_send.add_argument("--subject", required=True)
    p_send.add_argument("--body", required=True, help="Body text, or - for stdin")
    p_send.add_argument("--from", dest="from_addr", default="me")
    p_send.add_argument("--cc", default=None)
    p_send.add_argument("--bcc", default=None)

    # reply
    p_reply = subparsers.add_parser("reply", help="Reply to a message")
    p_reply.add_argument("-m", "--message-id", required=True)
    p_reply.add_argument("--body", required=True, help="Reply body, or - for stdin")
    p_reply.add_argument("--cc", default=None)
    p_reply.add_argument("--all", dest="reply_all", action="store_true")

    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    level = logging.DEBUG if args.verbose else logging.ERROR
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")

    service = get_gmail_service()

    commands = {
        "inbox": cmd_inbox,
        "search": cmd_search,
        "send": cmd_send,
        "reply": cmd_reply,
    }
    commands[args.command](service, args)


if __name__ == "__main__":
    main()
