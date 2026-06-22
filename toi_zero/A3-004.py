import sys
data = sys.stdin.read().split()
n = int(data[0])
us = []; vs = []
for i in range(n):
    x = int(data[1 + 2*i]); y = int(data[2 + 2*i])
    us.append(x + y); vs.append(x - y)
us.sort(); vs.sort()
mu = us[n // 2]; mv = vs[n // 2]
total = sum(abs(u - mu) for u in us) + sum(abs(v - mv) for v in vs)
print(total)
