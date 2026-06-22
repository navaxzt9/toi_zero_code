W, L, M, N = map(int, input().split())
best = W * L
for A in range(M, N + 1):
    waste = (L % A) * (W % A)
    if waste < best:
        best = waste
print(best)
