n = int(input())
start = (n // 10) * 10
print(" ".join(str(x) for x in range(start, -1, -10)))
