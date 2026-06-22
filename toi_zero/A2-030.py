grid = []
for _ in range(5):
    line = input().strip()
    parts = line.split()
    if len(parts) == 5:
        grid.append([int(x) for x in parts])
    else:
        grid.append([int(c) for c in line])
row_sum = [sum(r) for r in grid]
col_sum = [sum(grid[r][c] for r in range(5)) for c in range(5)]
bad_row = -1; bad_col = -1
for i in range(5):
    if row_sum[i] % 2 != 0:
        bad_row = i; break
for j in range(5):
    if col_sum[j] % 2 != 0:
        bad_col = j; break
print(f"{bad_row} {bad_col}")
