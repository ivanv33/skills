# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pytest",
#     "google-api-python-client",
#     "google-auth",
# ]
# ///

import argparse
import base64
import io
import sys
from email import message_from_bytes
from unittest.mock import MagicMock, patch

import pytest

from gmail_cli import (
    build_mime_message,
    cmd_inbox,
    cmd_reply,
    cmd_search,
    cmd_send,
    get_header,
    parse_args,
    read_body,
)


# --- parse_args ---


def test_parse_args_inbox_defaults():
    args = parse_args(["inbox"])
    assert args.command == "inbox"
    assert args.max_results == 10
    assert args.format == "summary"


def test_parse_args_inbox_custom():
    args = parse_args(["inbox", "-n", "5", "-f", "full"])
    assert args.max_results == 5
    assert args.format == "full"


def test_parse_args_search():
    args = parse_args(["search", "is:unread from:bob"])
    assert args.command == "search"
    assert args.query == "is:unread from:bob"


def test_parse_args_search_with_flags():
    args = parse_args(["search", "label:work", "-n", "3", "-f", "full"])
    assert args.query == "label:work"
    assert args.max_results == 3
    assert args.format == "full"


def test_parse_args_send_required():
    args = parse_args(["send", "--to", "a@b.com", "--subject", "Hi", "--body", "Hey"])
    assert args.command == "send"
    assert args.to == "a@b.com"
    assert args.subject == "Hi"
    assert args.body == "Hey"
    assert args.from_addr == "me"
    assert args.cc is None
    assert args.bcc is None


def test_parse_args_send_all_flags():
    args = parse_args([
        "send", "--to", "a@b.com", "--subject", "Hi", "--body", "Hey",
        "--from", "alias@b.com", "--cc", "c@b.com", "--bcc", "d@b.com",
    ])
    assert args.from_addr == "alias@b.com"
    assert args.cc == "c@b.com"
    assert args.bcc == "d@b.com"


def test_parse_args_send_missing_required():
    with pytest.raises(SystemExit):
        parse_args(["send", "--to", "a@b.com"])


def test_parse_args_reply_required():
    args = parse_args(["reply", "-m", "abc123", "--body", "Thanks"])
    assert args.command == "reply"
    assert args.message_id == "abc123"
    assert args.body == "Thanks"
    assert args.reply_all is False


def test_parse_args_reply_all_flag():
    args = parse_args(["reply", "-m", "abc", "--body", "ok", "--all"])
    assert args.reply_all is True


def test_parse_args_no_command():
    with pytest.raises(SystemExit):
        parse_args([])


# --- build_mime_message ---


def test_build_mime_basic():
    raw = build_mime_message(to="a@b.com", subject="Hi", body="Hello")
    decoded = base64.urlsafe_b64decode(raw)
    msg = message_from_bytes(decoded)
    assert msg["To"] == "a@b.com"
    assert msg["Subject"] == "Hi"
    assert msg["From"] == "me"
    assert msg.get_payload(decode=True).decode() == "Hello"


def test_build_mime_with_cc_bcc():
    raw = build_mime_message(
        to="a@b.com", subject="Hi", body="Hey",
        cc="c@b.com,d@b.com", bcc="e@b.com",
    )
    msg = message_from_bytes(base64.urlsafe_b64decode(raw))
    assert msg["Cc"] == "c@b.com,d@b.com"
    assert msg["Bcc"] == "e@b.com"


def test_build_mime_reply_headers():
    raw = build_mime_message(
        to="a@b.com", subject="Re: Hi", body="ok",
        in_reply_to="<orig@mail.com>", references="<orig@mail.com>",
    )
    msg = message_from_bytes(base64.urlsafe_b64decode(raw))
    assert msg["In-Reply-To"] == "<orig@mail.com>"
    assert msg["References"] == "<orig@mail.com>"


def test_build_mime_roundtrip():
    raw = build_mime_message(
        to="x@y.com", subject="Test", body="Body text",
        from_addr="sender@y.com", cc="cc@y.com",
        in_reply_to="<123@mail>", references="<123@mail>",
    )
    msg = message_from_bytes(base64.urlsafe_b64decode(raw))
    assert msg["To"] == "x@y.com"
    assert msg["From"] == "sender@y.com"
    assert msg["Subject"] == "Test"
    assert msg["Cc"] == "cc@y.com"
    assert msg["In-Reply-To"] == "<123@mail>"
    assert msg.get_payload(decode=True).decode() == "Body text"


# --- get_header ---


def test_get_header_found():
    msg = {"payload": {"headers": [
        {"name": "From", "value": "a@b.com"},
        {"name": "Subject", "value": "Hi"},
    ]}}
    assert get_header(msg, "From") == "a@b.com"
    assert get_header(msg, "subject") == "Hi"  # case-insensitive


def test_get_header_missing():
    msg = {"payload": {"headers": []}}
    assert get_header(msg, "From") is None


# --- read_body ---


def test_read_body_direct():
    assert read_body("hello") == "hello"


def test_read_body_stdin(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("from stdin"))
    assert read_body("-") == "from stdin"


# --- cmd_send ---


def _mock_service():
    service = MagicMock()
    service.users.return_value.messages.return_value.send.return_value.execute.return_value = {
        "id": "sent123", "threadId": "t1",
    }
    service.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [],
    }
    service.users.return_value.messages.return_value.get.return_value.execute.return_value = {
        "id": "msg1",
        "threadId": "t1",
        "snippet": "Hello...",
        "payload": {
            "headers": [
                {"name": "From", "value": "sender@x.com"},
                {"name": "To", "value": "me@x.com"},
                {"name": "Subject", "value": "Original"},
                {"name": "Date", "value": "Mon, 1 Jan 2024"},
                {"name": "Message-ID", "value": "<orig@mail.com>"},
            ],
        },
    }
    return service


def test_cmd_send_calls_api():
    service = _mock_service()
    args = argparse.Namespace(
        to="bob@x.com", subject="Hi", body="Hello",
        from_addr="me", cc=None, bcc=None,
    )
    cmd_send(service, args)
    service.users().messages().send.assert_called_once()
    call_kwargs = service.users().messages().send.call_args[1]
    assert call_kwargs["userId"] == "me"
    assert "raw" in call_kwargs["body"]


def test_cmd_send_stdin_body(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("stdin body"))
    service = _mock_service()
    args = argparse.Namespace(
        to="bob@x.com", subject="Hi", body="-",
        from_addr="me", cc=None, bcc=None,
    )
    cmd_send(service, args)
    raw = service.users().messages().send.call_args[1]["body"]["raw"]
    msg = message_from_bytes(base64.urlsafe_b64decode(raw))
    assert msg.get_payload(decode=True).decode() == "stdin body"


# --- cmd_inbox ---


def test_cmd_inbox_default(capsys):
    service = _mock_service()
    service.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}],
    }
    args = argparse.Namespace(max_results=10, format="summary")
    cmd_inbox(service, args)
    out = capsys.readouterr().out
    assert "msg1" in out
    assert "sender@x.com" in out


def test_cmd_inbox_empty(capsys):
    service = _mock_service()
    args = argparse.Namespace(max_results=10, format="summary")
    cmd_inbox(service, args)
    out = capsys.readouterr().out
    assert "No messages found" in out


# --- cmd_search ---


def test_cmd_search_passes_query():
    service = _mock_service()
    args = argparse.Namespace(query="is:unread", max_results=5, format="summary")
    cmd_search(service, args)
    service.users().messages().list.assert_called_once_with(
        userId="me", q="is:unread", maxResults=5,
    )


# --- cmd_reply ---


def test_cmd_reply_threads_correctly():
    service = _mock_service()
    args = argparse.Namespace(
        message_id="msg1", body="Thanks", cc=None, reply_all=False,
    )
    cmd_reply(service, args)
    send_call = service.users().messages().send.call_args[1]
    assert send_call["body"]["threadId"] == "t1"
    raw = base64.urlsafe_b64decode(send_call["body"]["raw"])
    msg = message_from_bytes(raw)
    assert msg["In-Reply-To"] == "<orig@mail.com>"
    assert msg["Subject"] == "Re: Original"
    assert msg["To"] == "sender@x.com"


def test_cmd_reply_no_double_re():
    service = _mock_service()
    # Override subject to already have Re:
    service.users.return_value.messages.return_value.get.return_value.execute.return_value[
        "payload"
    ]["headers"][2]["value"] = "Re: Original"
    args = argparse.Namespace(
        message_id="msg1", body="ok", cc=None, reply_all=False,
    )
    cmd_reply(service, args)
    raw = service.users().messages().send.call_args[1]["body"]["raw"]
    msg = message_from_bytes(base64.urlsafe_b64decode(raw))
    assert msg["Subject"] == "Re: Original"
    assert not msg["Subject"].startswith("Re: Re:")


def test_cmd_reply_all_adds_cc():
    service = _mock_service()
    # Add Cc header to original
    headers = service.users.return_value.messages.return_value.get.return_value.execute.return_value[
        "payload"
    ]["headers"]
    headers.append({"name": "Cc", "value": "cc@x.com"})
    args = argparse.Namespace(
        message_id="msg1", body="noted", cc=None, reply_all=True,
    )
    cmd_reply(service, args)
    raw = service.users().messages().send.call_args[1]["body"]["raw"]
    msg = message_from_bytes(base64.urlsafe_b64decode(raw))
    assert "me@x.com" in msg["Cc"]
    assert "cc@x.com" in msg["Cc"]


# --- full format & body extraction ---


def test_cmd_inbox_full_format(capsys):
    service = _mock_service()
    service.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}],
    }
    service.users.return_value.messages.return_value.get.return_value.execute.return_value = {
        "id": "msg1",
        "threadId": "t1",
        "snippet": "Hello...",
        "payload": {
            "headers": [
                {"name": "From", "value": "sender@x.com"},
                {"name": "Subject", "value": "Test Subject"},
                {"name": "Date", "value": "Mon, 1 Jan 2024"},
            ],
            "body": {
                "data": base64.urlsafe_b64encode(b"Full body text").decode(),
            },
        },
    }
    args = argparse.Namespace(max_results=10, format="full")
    cmd_inbox(service, args)
    out = capsys.readouterr().out
    assert "Test Subject" in out
    assert "Full body text" in out
    assert "sender@x.com" in out


def test_cmd_inbox_full_format_multipart(capsys):
    service = _mock_service()
    service.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}],
    }
    service.users.return_value.messages.return_value.get.return_value.execute.return_value = {
        "id": "msg1",
        "threadId": "t1",
        "snippet": "",
        "payload": {
            "headers": [
                {"name": "From", "value": "sender@x.com"},
                {"name": "Subject", "value": "Multi"},
                {"name": "Date", "value": "Mon, 1 Jan 2024"},
            ],
            "body": {"size": 0},
            "parts": [
                {
                    "mimeType": "text/html",
                    "body": {"data": base64.urlsafe_b64encode(b"<b>html</b>").decode()},
                },
                {
                    "mimeType": "text/plain",
                    "body": {"data": base64.urlsafe_b64encode(b"plain text body").decode()},
                },
            ],
        },
    }
    args = argparse.Namespace(max_results=10, format="full")
    cmd_inbox(service, args)
    out = capsys.readouterr().out
    assert "plain text body" in out
    assert "<b>html</b>" not in out


def test_cmd_inbox_full_format_no_body(capsys):
    service = _mock_service()
    service.users.return_value.messages.return_value.list.return_value.execute.return_value = {
        "messages": [{"id": "msg1"}],
    }
    service.users.return_value.messages.return_value.get.return_value.execute.return_value = {
        "id": "msg1",
        "threadId": "t1",
        "snippet": "",
        "payload": {
            "headers": [
                {"name": "Subject", "value": "Empty"},
            ],
            "body": {"size": 0},
        },
    }
    args = argparse.Namespace(max_results=10, format="full")
    cmd_inbox(service, args)
    out = capsys.readouterr().out
    assert "(no body)" in out


def test_cmd_search_empty(capsys):
    service = _mock_service()
    args = argparse.Namespace(query="nonexistent", max_results=10, format="summary")
    cmd_search(service, args)
    out = capsys.readouterr().out
    assert "No messages found" in out


# --- auth ---


def test_auth_missing_creds_exits():
    with patch("gmail_cli.google.auth.default") as mock_auth:
        mock_auth.side_effect = google_auth_error()
        with pytest.raises(SystemExit):
            from gmail_cli import get_gmail_service
            get_gmail_service()


def google_auth_error():
    import google.auth.exceptions
    return google.auth.exceptions.DefaultCredentialsError("no creds")


def test_auth_success():
    with patch("gmail_cli.google.auth.default") as mock_auth, \
         patch("gmail_cli.build") as mock_build:
        mock_creds = MagicMock()
        mock_creds.expired = False
        mock_auth.return_value = (mock_creds, "project")
        mock_build.return_value = MagicMock()
        from gmail_cli import get_gmail_service
        svc = get_gmail_service()
        mock_build.assert_called_once_with("gmail", "v1", credentials=mock_creds, cache_discovery=False)


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"] + sys.argv[1:]))
