import sys
data = sys.stdin.read().split()
i = 0
N = int(data[i]); i += 1
K = int(data[i]); i += 1
A1 = [int(data[i+k]) for k in range(N)]; i += N
A2 = [int(data[i+k]) for k in range(N)]; i += N
B1 = [int(data[i+k]) for k in range(N)]; i += N
B2 = [int(data[i+k]) for k in range(N)]; i += N

def max_sum_for_k(X, Y):
    # for each k=0..N, return max over pairs (X[i] + Y[k-1-i]) i=0..k-1 with X,Y sorted asc
    Xs = sorted(X)
    Ys = sorted(Y)
    res = [0] * (N + 1)
    for k in range(1, N + 1):
        m = 0
        for j in range(k):
            s = Xs[j] + Ys[k - 1 - j]
            if s > m: m = s
        res[k] = m
    return res

ms1 = max_sum_for_k(A1, B1)
ms2 = max_sum_for_k(A2, B2)
INF = 10**18
ans = INF
for k1 in range(N + 1):
    k2 = K - k1
    if k2 < 0 or k2 > N:
        continue
    cand = max(ms1[k1], ms2[k2])
    if cand < ans:
        ans = cand
print(ans)
