import sys
from collections import Counter
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
m = int(data[i]); i += 1
k = int(data[i]); i += 1
pos = Counter()
for _ in range(k):
    r = int(data[i]); i += 1
    c = int(data[i]); i += 1
    pos[(r, c)] += 1
best = 0
for r in range(n):
    for c in range(m):
        if pos[(r, c)] > 0:
            continue
        cnt = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0: continue
                cnt += pos.get((r + dr, c + dc), 0)
        if cnt > best:
            best = cnt
print(best)
