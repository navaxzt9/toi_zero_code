n = int(input())
p = list(map(int, input().split()))
sums = set()
for i in range(n):
    s = 0
    for j in range(i, n):
        s += p[j]
        sums.add(s)
print(len(sums))
