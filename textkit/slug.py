"""Turn a title into a URL-safe slug."""

import re


def slugify(text: str) -> str:
    """Lower-case the text, remove non-alphanumeric characters, and collapse spaces/separators into single hyphens."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
