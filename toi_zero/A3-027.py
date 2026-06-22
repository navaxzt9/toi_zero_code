import sys
data = sys.stdin.read().split("\n")
n, m = map(int, data[0].split())
grid = []
for i in range(n):
    line = data[1 + i]
    parts = line.split()
    if len(parts) == m:
        grid.append(parts)
    else:
        grid.append([c for c in line if c in "-*"])
new_grid = [row[:] for row in grid]
for r in range(1, n):
    for c in range(m):
        if grid[r-1][c] == "*":
            new_grid[r][c] = "*"
for row in new_grid:
    print(" ".join(row))
