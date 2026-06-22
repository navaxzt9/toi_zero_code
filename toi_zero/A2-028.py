n = int(input())
a = input().strip()
b = input().strip()
mismatch = sum(1 for x, y in zip(a, b) if int(x) + int(y) != 9)
if mismatch == 0:
    print("YES")
else:
    print(f"NO {mismatch}")
