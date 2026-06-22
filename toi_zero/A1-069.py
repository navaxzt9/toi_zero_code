n = int(input())
m = int(input())
top = (n + 1) // 2
for i in range(n):
    ch = "A" if i < top else "K"
    print(" ".join([ch] * m))
