"""Thin wrapper around the Claude API. All model calls go through here."""
import json
import os
import re

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("TUTOR_MODEL", "claude-sonnet-5-5")
_client = None


def client() -> Anthropic:
    global _client
    if _client is None:
        _client = Anthropic()  # reads ANTHROPIC_API_KEY from env
    return _client


def ask(system: str, user: str, max_tokens: int = 1500) -> str:
    resp = client().messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(b.text for b in resp.content if b.type == "text")


def ask_json(system: str, user: str, max_tokens: int = 1500):
    """Ask for JSON only; strip code fences and parse."""
    text = ask(system + "\nReturn ONLY valid JSON. No prose, no markdown fences.", user, max_tokens)
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()
    return json.loads(text)
