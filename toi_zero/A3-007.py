L, N = map(int, input().split())
j = 1
while j * L * (j * L + 1) // 2 < N:
    j += 1
print(j)
