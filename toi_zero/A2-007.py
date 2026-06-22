import sys
from collections import defaultdict
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    L = [0] * (N + 1)  # left (min x)
    R = [0] * (N + 1)  # right (max x)
    for i in range(1, N + 1):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        L[i] = min(a, b)
        R[i] = max(a, b)
    targets = set(int(data[idx + k]) for k in range(M))

    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        best = 0
        best_size = float('inf')
        for j in range(1, N + 1):
            if i == j: continue
            if L[j] < L[i] and R[j] > R[i]:
                sz = R[j] - L[j]
                if sz < best_size:
                    best_size = sz
                    best = j
        parent[i] = best

    children = defaultdict(list)
    roots = []
    for i in range(1, N + 1):
        if parent[i]:
            children[parent[i]].append(i)
        else:
            roots.append(i)

    # Iterative post-order
    order = []
    visited = [False] * (N + 1)
    for r in roots:
        stack = [(r, False)]
        while stack:
            node, done = stack.pop()
            if done:
                order.append(node)
                continue
            if visited[node]: continue
            visited[node] = True
            stack.append((node, True))
            for c in children[node]:
                stack.append((c, False))

    subtree_size = [0] * (N + 1)
    target_count = [0] * (N + 1)
    for v in order:
        s = 1
        t = 1 if v in targets else 0
        for c in children[v]:
            s += subtree_size[c]
            t += target_count[c]
        subtree_size[v] = s
        target_count[v] = t

    INF = (10**18, 10**18)
    dp = [(0, 0)] * (N + 1)
    choice = [0] * (N + 1)  # 0 = pick v, 1 = don't pick

    for v in order:
        if target_count[v] == 0:
            dp[v] = (0, 0)
            choice[v] = 1  # don't pick
            continue
        cost_A = (1, subtree_size[v] - target_count[v])
        if v in targets:
            dp[v] = cost_A; choice[v] = 0
            continue
        # Option B: don't pick v (v not target)
        sb_picks = 0; sb_extras = 0
        for c in children[v]:
            if target_count[c] > 0:
                sb_picks += dp[c][0]
                sb_extras += dp[c][1]
        cost_B = (sb_picks, sb_extras)
        if cost_A <= cost_B:
            dp[v] = cost_A; choice[v] = 0
        else:
            dp[v] = cost_B; choice[v] = 1

    selected = []
    stack = []
    for r in roots:
        if target_count[r] > 0:
            stack.append(r)
    while stack:
        v = stack.pop()
        if choice[v] == 0:
            selected.append(v)
        else:
            for c in children[v]:
                if target_count[c] > 0:
                    stack.append(c)
    selected.sort()
    print(len(selected))
    print(" ".join(map(str, selected)))

main()
