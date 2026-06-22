import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    dists = sorted((int(x) for x in data[1:n+1]), reverse=True)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + dists[i]

    INF = 10**18
    max_drone = 200
    # dp_next[i] = dp[i][j+1]; dp_cur[i] = dp[i][j].
    dp_next = [INF] * (n + 1)
    dp_next[n] = 0
    dp_cur = [INF] * (n + 1)
    dp_cur[n] = 0

    for j in range(max_drone, 0, -1):
        dp_cur = [INF] * (n + 1)
        dp_cur[n] = 0
        for i in range(n - 1, -1, -1):
            best = INF
            di = dists[i]
            pi = prefix[i]
            kmax = 10 if n - i >= 10 else n - i
            for k in range(1, kmax + 1):
                bs = prefix[i + k] - pi
                cost = j * (2 * bs - di)
                rest = dp_next[i + k]
                if rest < INF:
                    tot = cost + rest
                    if tot < best:
                        best = tot
            dp_cur[i] = best
        dp_next = dp_cur
    print(dp_cur[0])

main()
