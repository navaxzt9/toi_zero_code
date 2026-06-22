import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    segs = []  # (depth, length)
    cur_depth = 0
    for _ in range(N):
        D = int(data[idx]); idx += 1
        L = int(data[idx]); idx += 1
        cur_depth += D
        segs.append((cur_depth, L))
    queries = [int(data[idx+k]) for k in range(Q)]

    order = sorted(range(N), key=lambda i: -segs[i][0])
    parent = list(range(N))
    sum_arr = [0]*N
    active = [False]*N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    max_sum = 0
    events_d = []
    events_s = []

    i = 0
    while i < N:
        d_curr = segs[order[i]][0]
        j = i
        while j < N and segs[order[j]][0] == d_curr:
            ix = order[j]
            sum_arr[ix] = segs[ix][1]
            active[ix] = True
            for nb in (ix - 1, ix + 1):
                if 0 <= nb < N and active[nb]:
                    ra = find(ix); rb = find(nb)
                    if ra != rb:
                        parent[ra] = rb
                        sum_arr[rb] += sum_arr[ra]
            r = find(ix)
            if sum_arr[r] > max_sum:
                max_sum = sum_arr[r]
            j += 1
        events_d.append(d_curr)
        events_s.append(max_sum)
        i = j

    out = []
    n_ev = len(events_s)
    for W in queries:
        lo, hi = 0, n_ev
        while lo < hi:
            mid = (lo + hi) // 2
            if events_s[mid] >= W:
                hi = mid
            else:
                lo = mid + 1
        out.append(str(events_d[lo]) if lo < n_ev else "0")
    sys.stdout.write("\n".join(out) + "\n")

main()
