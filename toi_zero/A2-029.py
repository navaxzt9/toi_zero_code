n = int(input())
out = []
for r in range(n):
    row = []
    for c in range(r + 1):
        if c == 0 or c == r or r == n - 1:
            row.append("0")
        else:
            row.append("1")
    out.append("".join(row))
print("\n".join(out))
