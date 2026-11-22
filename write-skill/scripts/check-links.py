#!/usr/bin/env python3
"""Check relative links and #anchors across skills.

Usage: check-links.py [skills-dir]  (defaults to the directory holding write-skill)
Exits 1 and prints each broken link when any are found.
"""

import re
import sys
from pathlib import Path

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    return INLINE_CODE.sub("", FENCE.sub("", text))


def slug(heading: str) -> str:
    """GitHub-style heading anchor."""
    heading = re.sub(r"[`*_]", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).parents[2]).resolve()
    files = sorted(root.rglob("*.md"))
    anchors = {f: {slug(h) for h in HEADING.findall(strip_code(f.read_text()))} for f in files}

    broken = []
    for f in files:
        for target in LINK.findall(strip_code(f.read_text())):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue  # http:, mailto:, etc.
            path, _, anchor = target.partition("#")
            dest = (f.parent / path).resolve() if path else f
            if not dest.exists():
                broken.append(f"{f.relative_to(root)}: missing file {target}")
            elif anchor and dest.suffix == ".md" and anchor not in anchors.get(dest, set()):
                broken.append(f"{f.relative_to(root)}: missing anchor {target}")

    print("\n".join(broken) or f"All links resolve in {len(files)} files.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
