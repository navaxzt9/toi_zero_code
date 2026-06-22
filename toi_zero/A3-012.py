import sys
data = sys.stdin.read().split()
n = int(data[0]); s = int(data[1])
nxt = [0] * (n + 1)
for i in range(1, n + 1):
    nxt[i] = int(data[1 + i])
visited = set()
cur = s
count = 0
while cur != 0 and cur not in visited:
    visited.add(cur)
    count += 1
    cur = nxt[cur]
print(count)
