import sys
data = sys.stdin.read().split()
n = int(data[0])
covered = [False] * 360
for i in range(n):
    a = int(data[1 + 2*i]); b = int(data[2 + 2*i])
    if a < b:
        for k in range(a, b):
            covered[k] = True
    else:
        for k in range(a, 360):
            covered[k] = True
        for k in range(0, b):
            covered[k] = True
if all(covered):
    print(360)
else:
    # find max contiguous run of True with wraparound
    best = 0
    cur = 0
    for c in covered + covered:
        if c:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    best = min(best, 360)
    print(best)
