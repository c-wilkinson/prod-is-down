#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []

for md in root.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for target in pattern.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (md.parent / clean).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{md.relative_to(root)} -> escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{md.relative_to(root)} -> missing: {target}")

if errors:
    print("Broken links:")
    print("\n".join(f"  - {e}" for e in errors))
    sys.exit(1)

pages = list(root.rglob("*.md"))
print(f"OK: {len(pages)} Markdown files checked.")
