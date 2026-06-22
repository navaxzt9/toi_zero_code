import sys
data = sys.stdin.read().split()
n = int(data[0])
hs = [int(x) for x in data[1:n+1]]
big = sum(1 for h in hs if h > 18)
small = n - big
if big == 0:
    print(small)
else:
    print(max(big + small, 2 * big - 1))
