"""Turn a title into a URL-safe slug."""

import re


def slugify(text: str) -> str:
    """Lower-case the text, keep only letters and digits, and join with single hyphens."""
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)
    return "-".join(words)
