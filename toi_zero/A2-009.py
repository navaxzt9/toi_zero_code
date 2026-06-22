import sys
data = sys.stdin.read().split()
i = 0
N = int(data[i]); i += 1
C = int(data[i]); i += 1
table = [[0]*(N+1) for _ in range(N+1)]
for r in range(1, N+1):
    for c in range(1, N+1):
        table[r][c] = int(data[i]); i += 1
teams = list(range(1, N+1))
has_card = (C != 0)
while len(teams) > 1:
    nxt = []
    for k in range(0, len(teams), 2):
        a, b = teams[k], teams[k+1]
        w = table[a][b]
        if has_card and C in (a, b):
            opp = b if a == C else a
            if w == opp:
                w = C
                has_card = False
        nxt.append(w)
    teams = nxt
print(teams[0])
