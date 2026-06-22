import math
from collections import deque
N = int(input())
if N == 1:
    print(0)
else:
    # find row r and position p
    r = math.ceil(math.sqrt(N))
    p = N - (r - 1) ** 2
    # BFS to (1,1) on triangular grid
    target = (1, 1)
    start = (r, p)
    visited = {start: 0}
    dq = deque([start])
    while dq:
        cr, cp = dq.popleft()
        d = visited[(cr, cp)]
        if (cr, cp) == target:
            print(d)
            break
        nbrs = []
        if cp - 1 >= 1:
            nbrs.append((cr, cp - 1))
        if cp + 1 <= 2 * cr - 1:
            nbrs.append((cr, cp + 1))
        if cp % 2 == 1:  # up triangle
            if cr + 1 <= 2000 and cp + 1 <= 2 * (cr + 1) - 1:
                # below: but only if exists
                pass  # don't go down for shortest path to (1,1)
        else:  # even = down triangle, can go up
            if cr - 1 >= 1 and cp - 1 >= 1 and cp - 1 <= 2 * (cr - 1) - 1:
                nbrs.append((cr - 1, cp - 1))
        for nb in nbrs:
            if nb not in visited:
                visited[nb] = d + 1
                dq.append(nb)
