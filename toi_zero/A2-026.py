n = int(input())
over = 0
heaviest_name = ""
heaviest_w = -10**18
for _ in range(n):
    parts = input().split()
    name = " ".join(parts[:-1])
    w = int(parts[-1])
    if w > 15:
        over += 1
    if w > heaviest_w:
        heaviest_w = w
        heaviest_name = name
print(over)
print(f"{heaviest_name} {heaviest_w}")
