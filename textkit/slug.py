"""Turn a title into a URL-safe slug."""

import re


def slugify(text: str) -> str:
    """Lower-case the text, replace non-alphanumeric runs with single hyphens, and strip ends."""
    return re.sub(r"[\W_]+", "-", text.lower()).strip("-")
