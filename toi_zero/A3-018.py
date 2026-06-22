L, N = map(int, input().split())
total = 0
emptied = 0
for k in range(1, L + 1):
    total += k * k
    if total <= N:
        emptied = k
    else:
        break
print(L - emptied)
