import sys
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
m = int(data[i]); i += 1
k = int(data[i]); i += 1
mines = set()
for _ in range(k):
    r = int(data[i]); i += 1
    c = int(data[i]); i += 1
    mines.add((r, c))
out = []
for r in range(n):
    row = []
    for c in range(m):
        if (r, c) in mines:
            row.append("x")
        else:
            cnt = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0: continue
                    if (r + dr, c + dc) in mines:
                        cnt += 1
            row.append(str(cnt))
    out.append(" ".join(row))
print("\n".join(out))
