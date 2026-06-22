n = int(input())
shots = []
for _ in range(n):
    x, y, d = map(int, input().split())
    shots.append((x, y, d))
best = None
for tx in range(1, 1000):
    for ty in range(1, 1000):
        ok = True
        for x, y, d in shots:
            if (tx - x) ** 2 + (ty - y) ** 2 != d * d:
                ok = False
                break
        if ok:
            best = (tx, ty)
            break
    if best:
        break
print(f"{best[0]} {best[1]}")
