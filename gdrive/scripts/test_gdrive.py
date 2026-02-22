# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
#     "google-api-python-client",
#     "google-auth",
# ]
# ///

import argparse
import sys
from unittest.mock import MagicMock, patch

import pytest

from gdrive import (
    _export_default,
    _export_tab,
    cmd_get,
    cmd_query,
    get_drive_service,
    parse_args,
    parse_doc_input,
)


# --- parse_doc_input ---


def test_parse_raw_doc_id():
    doc_id, tab_id = parse_doc_input("18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv")
    assert doc_id == "18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv"
    assert tab_id is None


def test_parse_url_without_tab():
    url = "https://docs.google.com/document/d/18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv/edit"
    doc_id, tab_id = parse_doc_input(url)
    assert doc_id == "18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv"
    assert tab_id is None


def test_parse_url_with_tab():
    url = "https://docs.google.com/document/d/18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv/edit?tab=t.j91ypq8vpc0b"
    doc_id, tab_id = parse_doc_input(url)
    assert doc_id == "18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv"
    assert tab_id == "t.j91ypq8vpc0b"


def test_parse_url_with_tab_and_other_params():
    url = "https://docs.google.com/document/d/18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv/edit?tab=t.abc123&pli=1"
    doc_id, tab_id = parse_doc_input(url)
    assert doc_id == "18Xc32LOIAARhx1Y3fnJMeDxFCsF_i3Vv"
    assert tab_id == "t.abc123"


def test_parse_bad_host():
    with pytest.raises(ValueError, match="Not a Google Docs URL"):
        parse_doc_input("https://evil.com/document/d/abc123/edit")


def test_parse_missing_doc_id_in_url():
    with pytest.raises(ValueError, match="Could not extract document ID"):
        parse_doc_input("https://docs.google.com/spreadsheets/d/abc123/edit")


# --- parse_args ---


def test_parse_args_get_defaults():
    args = parse_args(["get", "abc123"])
    assert args.command == "get"
    assert args.doc_id == "abc123"
    assert args.output is None
    assert args.format == "md"


def test_parse_args_get_with_url():
    url = "https://docs.google.com/document/d/abc123/edit?tab=t.xyz"
    args = parse_args(["get", url])
    assert args.doc_id == url


def test_parse_args_query():
    args = parse_args(["query", "My Notes"])
    assert args.command == "query"
    assert args.name == "My Notes"
    assert args.meta is False


def test_parse_args_query_meta():
    args = parse_args(["query", "My Notes", "--meta"])
    assert args.command == "query"
    assert args.meta is True


def test_parse_args_no_command():
    with pytest.raises(SystemExit):
        parse_args([])


# --- cmd_query ---


def test_cmd_query_no_meta():
    service = MagicMock()
    service.files.return_value.list.return_value.execute.return_value = {
        "files": [{"id": "doc1", "name": "My Notes"}]
    }
    args = argparse.Namespace(name="Notes", meta=False)
    cmd_query(service, args)
    service.files().list.assert_called_once_with(
        q="name contains 'Notes' and mimeType='application/vnd.google-apps.document' and trashed=false",
        pageSize=10,
        fields="nextPageToken, files(id, name)",
    )


def test_cmd_query_with_meta():
    service = MagicMock()
    service.files.return_value.list.return_value.execute.return_value = {
        "files": [
            {
                "id": "doc1",
                "name": "My Notes",
                "createdTime": "2025-01-01T00:00:00.000Z",
                "modifiedTime": "2025-01-15T10:30:00.000Z",
                "owners": [{"emailAddress": "user@gmail.com"}],
                "permissions": [
                    {"emailAddress": "user@gmail.com", "role": "owner"},
                    {"emailAddress": "friend@gmail.com", "role": "writer"},
                ],
                "webViewLink": "https://docs.google.com/document/d/doc1/edit",
            }
        ]
    }
    args = argparse.Namespace(name="Notes", meta=True)
    cmd_query(service, args)
    service.files().list.assert_called_once_with(
        q="name contains 'Notes' and mimeType='application/vnd.google-apps.document' and trashed=false",
        pageSize=10,
        fields="nextPageToken, files(id, name, createdTime, modifiedTime, owners(emailAddress), permissions(emailAddress, role), webViewLink)",
    )


def test_cmd_query_no_results():
    service = MagicMock()
    service.files.return_value.list.return_value.execute.return_value = {"files": []}
    args = argparse.Namespace(name="Nothing", meta=False)
    cmd_query(service, args)  # should not raise


# --- export dispatch ---


@patch("gdrive._export_default")
def test_cmd_get_raw_id_calls_default(mock_default):
    mock_default.return_value = b"# Hello"
    service = MagicMock()
    args = argparse.Namespace(doc_id="abc123", output=None, format="md")
    cmd_get(service, args)
    mock_default.assert_called_once_with(service, "abc123", "text/markdown")


@patch("gdrive._export_tab")
def test_cmd_get_url_with_tab_calls_tab(mock_tab):
    mock_tab.return_value = b"# Tab Content"
    service = MagicMock()
    url = "https://docs.google.com/document/d/abc123/edit?tab=t.xyz"
    args = argparse.Namespace(doc_id=url, output=None, format="md")
    cmd_get(service, args)
    mock_tab.assert_called_once_with("abc123", "t.xyz", "md")


@patch("gdrive._export_tab")
def test_cmd_get_tab_error_exits(mock_tab):
    mock_tab.side_effect = SystemExit(1)
    service = MagicMock()
    url = "https://docs.google.com/document/d/abc123/edit?tab=t.xyz"
    args = argparse.Namespace(doc_id=url, output=None, format="md")
    with pytest.raises(SystemExit):
        cmd_get(service, args)


# --- _export_default ---


def test_export_default_downloads():
    service = MagicMock()
    mock_request = MagicMock()
    service.files.return_value.export_media.return_value = mock_request

    with patch("gdrive.MediaIoBaseDownload") as mock_dl_cls:
        mock_dl = MagicMock()
        mock_dl.next_chunk.return_value = (None, True)
        mock_dl_cls.return_value = mock_dl

        with patch("gdrive.io.BytesIO") as mock_bio:
            mock_buf = MagicMock()
            mock_buf.getvalue.return_value = b"content"
            mock_bio.return_value = mock_buf

            result = _export_default(service, "doc1", "text/markdown")

    assert result == b"content"
    service.files().export_media.assert_called_once_with(fileId="doc1", mimeType="text/markdown")


# --- _export_tab ---


@patch("gdrive.google.auth.default")
@patch("gdrive.google.auth.transport.requests.AuthorizedSession")
def test_export_tab_success(mock_session_cls, mock_auth):
    mock_creds = MagicMock()
    mock_auth.return_value = (mock_creds, "project")

    mock_session = MagicMock()
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.content = b"tab content"
    mock_session.get.return_value = mock_resp
    mock_session_cls.return_value = mock_session

    result = _export_tab("doc1", "t.abc", "md")
    assert result == b"tab content"
    mock_session.get.assert_called_once_with(
        "https://docs.google.com/document/export?format=markdown&id=doc1&tab=t.abc"
    )


@patch("gdrive.google.auth.default")
@patch("gdrive.google.auth.transport.requests.AuthorizedSession")
def test_export_tab_markdown_fallback_to_txt(mock_session_cls, mock_auth):
    mock_creds = MagicMock()
    mock_auth.return_value = (mock_creds, "project")

    mock_session = MagicMock()
    fail_resp = MagicMock()
    fail_resp.status_code = 400
    ok_resp = MagicMock()
    ok_resp.status_code = 200
    ok_resp.content = b"txt fallback"
    mock_session.get.side_effect = [fail_resp, ok_resp]
    mock_session_cls.return_value = mock_session

    result = _export_tab("doc1", "t.abc", "md")
    assert result == b"txt fallback"
    assert mock_session.get.call_count == 2


@patch("gdrive.google.auth.default")
@patch("gdrive.google.auth.transport.requests.AuthorizedSession")
def test_export_tab_http_error_exits(mock_session_cls, mock_auth):
    mock_creds = MagicMock()
    mock_auth.return_value = (mock_creds, "project")

    mock_session = MagicMock()
    mock_resp = MagicMock()
    mock_resp.status_code = 403
    mock_resp.text = "Forbidden"
    mock_session.get.return_value = mock_resp
    mock_session_cls.return_value = mock_session

    with pytest.raises(SystemExit):
        _export_tab("doc1", "t.abc", "pdf")


# --- auth ---


def test_auth_missing_creds_exits():
    with patch("gdrive.google.auth.default") as mock_auth:
        import google.auth.exceptions
        mock_auth.side_effect = google.auth.exceptions.DefaultCredentialsError("no creds")
        with pytest.raises(SystemExit):
            get_drive_service()


def test_auth_success():
    with patch("gdrive.google.auth.default") as mock_auth, \
         patch("gdrive.build") as mock_build:
        mock_creds = MagicMock()
        mock_creds.expired = False
        mock_auth.return_value = (mock_creds, "project")
        mock_build.return_value = MagicMock()
        svc = get_drive_service()
        mock_build.assert_called_once_with("drive", "v3", credentials=mock_creds, cache_discovery=False)


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"] + sys.argv[1:]))
