n = int(input())
grid = list(map(int, input().split()))
s = input().strip()
pos = grid.index(1)
treasure = grid.index(2)
for c in s:
    nxt = pos + (1 if c == "R" else -1)
    if nxt < 0 or nxt >= n:
        continue
    grid[pos] = 0
    pos = nxt
    if grid[pos] == 2:
        grid[pos] = 1
        break
    grid[pos] = 1
print(" ".join(map(str, grid)))
