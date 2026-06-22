import sys
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
m = int(data[i]); i += 1
rules = []
trigger_for = [[] for _ in range(n + 1)]
needed = [0] * m
target = [0] * m
for r in range(m):
    k = int(data[i]); i += 1
    needed[r] = k
    for _ in range(k):
        s = int(data[i]); i += 1
        trigger_for[s].append(r)
    target[r] = int(data[i]); i += 1

on = [False] * (n + 1)
on[1] = True
queue = [1]
remaining = needed[:]
while queue:
    nxt = []
    for s in queue:
        for r in trigger_for[s]:
            remaining[r] -= 1
            if remaining[r] == 0:
                t = target[r]
                if not on[t]:
                    on[t] = True
                    nxt.append(t)
    queue = nxt
print(sum(on))
