import sys
input = sys.stdin.readline
n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]
from collections import defaultdict
g1 = defaultdict(list)  # x-y groups (main diagonal)
g2 = defaultdict(list)  # x+y groups (anti-diagonal)
for x, y in pts:
    g1[x - y].append(x)
    g2[x + y].append(x)
best = 0
for d in (g1, g2):
    for xs in d.values():
        if len(xs) >= 2:
            best = max(best, max(xs) - min(xs))
print(best)
