import sys
sys.setrecursionlimit(10000)
data = sys.stdin.read().split()
n = int(data[0])
sticks = []
for i in range(n):
    a = int(data[1 + 4*i]); l = int(data[2 + 4*i])
    b = int(data[3 + 4*i]); r = int(data[4 + 4*i])
    sticks.append((a, l, b, r))

# DP: solve(i) returns (balanced_weight, added)
memo = {}
def solve(i):
    if i in memo:
        return memo[i]
    a, l, b, r = sticks[i]
    if a == 1:
        lw, la = l, 0
    else:
        lw, la = solve(l - 1)
    if b == 1:
        rw, ra = r, 0
    else:
        rw, ra = solve(r - 1)
    bw = 2 * max(lw, rw)
    added = la + ra + (max(lw, rw) - lw) + (max(lw, rw) - rw)
    memo[i] = (bw, added)
    return memo[i]

_, total = solve(0)
print(total)
