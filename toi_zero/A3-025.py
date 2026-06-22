import sys
data = sys.stdin.read().split()
i = 0
N = int(data[i]); i += 1
W = int(data[i]); i += 1
L = int(data[i]); i += 1
valid_planks = []
for _ in range(N):
    k = int(data[i]); i += 1
    holes = [int(data[i+j]) for j in range(k)]; i += k
    v = [False] * (W + 2)
    for h in holes:
        lo = max(1, h - L); hi = min(W, h + L)
        for p in range(lo, hi + 1):
            v[p] = True
    valid_planks.append(v)
ok = False
for p in range(1, W + 1):
    if all(v[p] for v in valid_planks):
        ok = True
        break
print(1 if ok else 0)
