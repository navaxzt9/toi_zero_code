import sys
data = sys.stdin.buffer.read().split()
i = 0
N = int(data[i]); i += 1
M = int(data[i]); i += 1
events = []
for _ in range(M):
    s = int(data[i]); i += 1
    t = int(data[i]); i += 1
    events.append((s, 1))
    events.append((t + 1, -1))
events.sort()
cur = 0; best = 0
for _, d in events:
    cur += d
    if cur > best:
        best = cur
print(best)
