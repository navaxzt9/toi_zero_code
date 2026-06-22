import sys
data = sys.stdin.read().split()
i = 0
R = int(data[i]); i += 1
C = int(data[i]); i += 1
rr = int(data[i]); i += 1
rc = int(data[i]); i += 1
N = int(data[i]); i += 1
infs = []
for _ in range(N):
    a = int(data[i]); i += 1
    b = int(data[i]); i += 1
    infs.append((a, b))
def cheby_min(r, c):
    best = 10**9
    for a, b in infs:
        d = max(abs(r - a), abs(c - b))
        if d < best:
            best = d
    return best
def risk_at(r, c):
    d = cheby_min(r, c)
    if d == 0: return 100
    if d == 1: return 60
    if d == 2: return 20
    return 0
safe = sum(1 for r in range(R) for c in range(C) if risk_at(r, c) == 0)
print(safe)
print(f"{risk_at(rr, rc)}%")
