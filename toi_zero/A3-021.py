import sys
data = sys.stdin.read().split()
n = int(data[0]); k = int(data[1])
S = [int(x) for x in data[2:2+n]]
smin = min(S)
if k == 1:
    print(n)
else:
    survivors = 0
    for s in S:
        if s == smin:
            survivors += 1
        elif (k - 1) * s < k * smin:
            survivors += 1
    print(survivors)
