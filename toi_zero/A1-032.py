n = int(input())
for k in (n, n-2, n-4):
    print("*" * max(k, 0))
