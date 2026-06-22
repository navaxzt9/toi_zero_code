import sys
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
p = float(data[i]); i += 1
grid = []
for _ in range(n):
    row = [int(data[i+k]) for k in range(n)]; i += n
    grid.append(row)
total_bad_tiles = 0
total_bad_points = 0
bad_tiles_col = [0]*n
bad_points_col = [0]*n
out = []
for r in range(n):
    bt = sum(1 for x in grid[r] if x > 0)
    bp = sum(grid[r])
    out.append(" ".join(str(x) for x in grid[r]) + f" {bt} {bp}")
    total_bad_tiles += bt
    total_bad_points += bp
    for c in range(n):
        if grid[r][c] > 0:
            bad_tiles_col[c] += 1
        bad_points_col[c] += grid[r][c]
out.append(" ".join(str(x) for x in bad_tiles_col))
out.append(" ".join(str(x) for x in bad_points_col))
fine = total_bad_points * p
out.append(f"{total_bad_tiles} {total_bad_points} {fine:.2f}")
print("\n".join(out))
