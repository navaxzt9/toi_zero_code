import sys
data = sys.stdin.read().split()
n = int(data[0]); k = int(data[1])
c = [int(x) for x in data[2:2+n]]

def at_most(K):
    if K < 0: return 0
    cnt = {}
    distinct = 0
    l = 0
    total = 0
    for r in range(n):
        x = c[r]
        if cnt.get(x, 0) == 0:
            distinct += 1
        cnt[x] = cnt.get(x, 0) + 1
        while distinct > K:
            y = c[l]
            cnt[y] -= 1
            if cnt[y] == 0:
                distinct -= 1
            l += 1
        total += r - l + 1
    return total

ans = n * (n + 1) // 2 - at_most(k - 1)
print(ans)
