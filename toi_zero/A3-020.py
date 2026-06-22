H1, H2, B1, B2 = map(int, input().split())
X, Y = map(int, input().split())
best = 0
for a in range(min(H1, B1) + 1):
    for b in range(min(H2, B2) + 1):
        same = a + b
        max_c = min(H1 - a, B2 - b)
        max_d = min(H2 - b, B1 - a)
        diff_max = max_c + max_d
        sales = min(same, X) + min(diff_max, Y)
        if sales > best:
            best = sales
print(best)
