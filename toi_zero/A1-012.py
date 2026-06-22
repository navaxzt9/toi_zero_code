n = int(input())
op = input().strip()
r = int(str(n)[::-1])
if op == "+":
    print(f"{n} + {r} = {n + r}")
else:
    print(f"{n} * {r} = {n * r}")
