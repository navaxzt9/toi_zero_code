import sys
data = sys.stdin.read().split()
n = int(data[0])
hs = sorted(int(x) for x in data[1:n+1])
total = 0
for j, h in enumerate(hs, 1):
    total += h * (n - j + 1)
print(2 * total)
