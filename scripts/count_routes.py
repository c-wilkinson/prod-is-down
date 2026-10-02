#!/usr/bin/env python3
from pathlib import Path
import re
from collections import deque

root = Path(__file__).resolve().parents[1]
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

if not (root / "README.md").exists():
    print("No game content yet; finish-point check skipped.")
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
if not endings:
    raise SystemExit("Game has no finish points under endings/")

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
    raise SystemExit("Unreachable finish points: " + ", ".join(sorted(missing_endings)))

print(f"Reachable finish points: {len(endings)}/{len(endings)}")
print(f"Reachable game pages: {len(reachable)}/{len(graph)}")
