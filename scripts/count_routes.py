#!/usr/bin/env python3
from pathlib import Path
import re
from collections import deque

root = Path(__file__).resolve().parents[1]
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MAX_PATHS = 5000
MAX_DEPTH = 40

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

# First prove reachability without enumerating every route.
reachable = {"README.md"}
q = deque(["README.md"])
while q:
    node = q.popleft()
    for nxt in graph.get(node, []):
        if nxt not in reachable:
            reachable.add(nxt)
            q.append(nxt)

missing_endings = endings - reachable
if missing_endings:
    raise SystemExit("Unreachable endings: " + ", ".join(sorted(missing_endings)))

# Then establish that the game has comfortably more than 50 distinct simple routes.
count = 0

def walk(node, seen, depth):
    global count
    if count >= MAX_PATHS:
        return
    if node in endings:
        count += 1
        return
    if depth >= MAX_DEPTH:
        return
    for nxt in graph.get(node, []):
        if nxt not in seen:
            walk(nxt, seen | {nxt}, depth + 1)
            if count >= MAX_PATHS:
                return

walk("README.md", {"README.md"}, 0)
suffix = "+" if count >= MAX_PATHS else ""
print(f"Playable simple routes found: {count}{suffix}")
print(f"Reachable endings: {len(endings)}/{len(endings)}")
print(f"Reachable game pages: {len(reachable)}/{len(graph)}")

if count < 50:
    raise SystemExit("Expected at least 50 playable routes")
