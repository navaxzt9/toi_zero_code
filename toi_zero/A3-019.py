import sys
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
l = int(data[i]); i += 1
h = [int(data[i+k]) for k in range(n)]; i += n
custs = [int(data[i+k]) for k in range(l)]
prefix_max = [0] * (n + 1)
for k in range(n):
    prefix_max[k+1] = max(prefix_max[k], h[k])
out = []
for a in custs:
    if a == 1:
        out.append(0)
    else:
        m = prefix_max[a-1]
        out.append(max(0, m + 1 - h[a-1]))
print("\n".join(map(str, out)))
