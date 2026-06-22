import sys
data = sys.stdin.read().split()
i = 0
n = int(data[i]); i += 1
path1 = [int(x) for x in data[i:i+n]]; i += n
path2 = [int(x) for x in data[i:i+n]]; i += n

def gen_segs(path):
    prev = 1
    segs = []
    for x in path:
        segs.append((prev, x))
        prev = x
    return segs

s1 = gen_segs(path1)
s2 = gen_segs(path2)

def in_arc(a, b, x, n):
    bp = (b - a) % n
    xp = (x - a) % n
    return 0 < xp < bp

def cross(a1, b1, a2, b2, n):
    if {a1, b1} == {a2, b2}:
        return True  # same chord
    pts = {a1, b1, a2, b2}
    if len(pts) < 4:
        return False  # share one endpoint only
    return in_arc(a1, b1, a2, n) != in_arc(a1, b1, b2, n)

count = 0
for (a1, b1), (a2, b2) in zip(s1, s2):
    if cross(a1, b1, a2, b2, n):
        count += 1
print(count)
