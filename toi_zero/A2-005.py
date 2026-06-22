import sys
data = sys.stdin.read().split()
i = 0
W = int(data[i]); i += 1
H = int(data[i]); i += 1
M = int(data[i]); i += 1
N = int(data[i]); i += 1
xs = [int(x) for x in data[i:i+M]]; i += M
ys = [int(x) for x in data[i:i+N]]; i += N
xs = [0] + xs + [W]
ys = [0] + ys + [H]
dx = [xs[k+1] - xs[k] for k in range(len(xs)-1)]
dy = [ys[k+1] - ys[k] for k in range(len(ys)-1)]
first = second = 0
for a in dx:
    for b in dy:
        v = a * b
        if v > first:
            second = first
            first = v
        elif v > second:
            second = v
print(first, second)
