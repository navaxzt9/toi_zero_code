n = int(input())
c = 0
for _ in range(n):
    if input().strip() in "AEIOU":
        c += 1
print(c)
