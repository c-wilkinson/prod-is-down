#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

if not (root / "README.md").exists():
    print("No game content yet; route check skipped.")
    raise SystemExit(0)

def rel(p):
    return p.relative_to(root).as_posix()

graph = {}
for md in root.rglob("*.md"):
    rp = rel(md)
    if rp.startswith((".meta/", "DO_NOT_OPEN/")):
        continue
    targets = []
    for link in link_re.findall(md.read_text(encoding="utf-8")):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        dest = (md.parent / link.split("#", 1)[0]).resolve()
        if dest.exists() and dest.suffix == ".md":
            try:
                targets.append(rel(dest))
            except ValueError:
                pass
    graph[rp] = targets

endings = {p for p in graph if p.startswith("endings/")}
count = 0

def walk(node, seen, depth=0):
    global count
    if count >= MAX_PATHS:
        return
    if node in endings:
        count += 1
        return
    if depth >= 40:
        return
    for nxt in graph.get(node, []):
        if nxt not in seen:
            walk(nxt, seen | {nxt}, depth + 1)
            if count >= MAX_PATHS:
                return

walk("README.md", {"README.md"})
suffix = "+" if count >= MAX_PATHS else ""
print(f"Playable simple routes found: {count}{suffix}")
