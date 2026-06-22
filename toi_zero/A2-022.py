import sys
data = sys.stdin.read().split()
i = 0
L = int(data[i]); i += 1
N = int(data[i]); i += 1
bridges = []
for _ in range(N):
    a = int(data[i]); i += 1
    b = int(data[i]); i += 1
    bridges.append((a, b))
# sweep line: for each half-km position check how many bridges cover it
# bridges cover (a, b) exclusive endpoints
best = 0
events = []
for a, b in bridges:
    events.append((a, 1))
    events.append((b, -1))
events.sort(key=lambda e: (e[0], -e[1]))
# Count max overlap in open intervals
# Use coordinate compression: check midpoints between all boundary events
pts = set()
for a, b in bridges:
    pts.add(a)
    pts.add(b)
pts = sorted(pts)
# Check midpoints between consecutive unique boundary points
for k in range(len(pts) - 1):
    mid = (pts[k] + pts[k+1]) / 2
    cnt = sum(1 for a, b in bridges if a < mid < b)
    best = max(best, cnt)
# Also check positions just inside each bridge near boundaries
print(best)
