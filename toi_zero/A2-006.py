import sys
data = sys.stdin.read().split()
n = int(data[0])
grid = data[1:1+n]
reach = [[False]*n for _ in range(n)]
if grid[n-1][n-1] == ".":
    reach[n-1][n-1] = True
for r in range(n-1, -1, -1):
    for c in range(n-1, -1, -1):
        if grid[r][c] == "X":
            continue
        if r == n-1 and c == n-1:
            continue
        right = reach[r][c+1] if c+1 < n else False
        down = reach[r+1][c] if r+1 < n else False
        if right or down:
            reach[r][c] = True
count = sum(1 for r in range(n) for c in range(n) if reach[r][c])
print(count)
