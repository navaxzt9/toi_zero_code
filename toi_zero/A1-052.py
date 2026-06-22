n = int(input())
if n < 100 or n > 20000 or n % 100 != 0:
    print("ERROR")
else:
    parts = []
    for d in (1000, 500, 100):
        c, n = divmod(n, d)
        if c > 0:
            parts.append(f"{d} = {c}")
    print("\n".join(parts))
