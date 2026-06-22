import sys
data = sys.stdin.read().split()
i = 0
num = int(data[i]); i += 1
q = int(data[i]); i += 1
intervals = []
for _ in range(num):
    a = int(data[i]); i += 1
    b = int(data[i]); i += 1
    intervals.append((a, b))
queries = [int(data[i+k]) for k in range(q)]
# Use diff array on 0..1440
diff = [0] * 1443
for a, b in intervals:
    diff[a] += 1
    diff[b + 1] -= 1
# Prefix sum
for k in range(1, 1443):
    diff[k] += diff[k-1]
out = [str(diff[t]) for t in queries]
print(" ".join(out))
