"""Turn a title into a URL-safe slug."""

import re


def slugify(text: str) -> str:
    """Lower-case the text and join its words with single hyphens."""
    text = text.lower()
    cleaned = re.sub(r"[^a-z0-9]+", "-", text)
    return cleaned.strip("-")
