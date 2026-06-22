import sys
data = sys.stdin.read().split()
idx = 0
L = int(data[idx]); idx += 1
P = int(data[idx]); idx += 1
jr = int(data[idx]); idx += 1
jm = int(data[idx]); idx += 1
jf = int(data[idx]); idx += 1
points = {}
for _ in range(P):
    pos = int(data[idx]); idx += 1
    pts = int(data[idx]); idx += 1
    points[pos] = pts
def score(jump):
    s = 0
    pos = 0
    while pos <= L:
        if pos in points:
            s += points[pos]
        pos += jump
    return s
sr = score(jr); sm = score(jm); sf = score(jf)
best = max(sr, sm, sf)
out = []
if sr == best: out.append(f"Rabbit {sr}")
if sm == best: out.append(f"Monkey {sm}")
if sf == best: out.append(f"Frog {sf}")
print("\n".join(out))
