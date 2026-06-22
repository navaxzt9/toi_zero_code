from collections import Counter
n = int(input())
codes = list(map(int, input().split()))
cnt = Counter(codes)
unique = sorted(c for c, k in cnt.items() if k == 1)
print(" ".join(map(str, unique)))
