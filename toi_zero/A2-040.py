import sys
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
A = []
for _ in range(n):
    A.append([int(x) for x in data[i:i+n]]); i += n
B = []
for _ in range(n):
    B.append([int(x) for x in data[i:i+n]]); i += n
out = []
for r in range(n):
    out.append(" ".join(str(A[r][c] + B[r][c]) for c in range(n)))
print("\n".join(out))
