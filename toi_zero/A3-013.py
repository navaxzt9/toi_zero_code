import sys
data = sys.stdin.read().split()
n = int(data[0]); s = int(data[1])
heights = [int(data[2+i]) for i in range(n)]
min_walk = 0
max_walk = 0
for h in heights:
    div3 = (h % 3 == 0)
    div4 = (h % 4 == 0)
    if div3 and div4:
        # type 1: 10*h/3, type 2: 10*h/4
        w1 = 10 * h // 3
        w2 = 10 * h // 4
        min_walk += min(w1, w2)
        max_walk += max(w1, w2)
    elif div3:
        w = 10 * h // 3
        min_walk += w; max_walk += w
    else:  # div4
        w = 10 * h // 4
        min_walk += w; max_walk += w
print(s - max_walk, s - min_walk)
