a, b, d, r = map(int, input().split())
count = 0
for x in range(a, b + 1):
    if x % d == r:
        count += 1
print(count)
