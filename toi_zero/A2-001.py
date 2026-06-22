import sys
from fractions import Fraction

def build(touches):
    # source (0,0); touch k (1-indexed) at y = k%2 (odd top, even bottom)
    pts = [(0, 0)]
    for k, x in enumerate(touches, 1):
        pts.append((x, k % 2))
    segs = []
    for i in range(len(pts) - 1):
        segs.append((pts[i], pts[i+1]))
    return segs

def seg_intersect(a, b):
    # a, b are ((x1,y1),(x2,y2)) integer endpoints
    (x1, y1), (x2, y2) = a
    (x3, y3), (x4, y4) = b
    # parametric: P = a1 + t*(a2-a1), Q = b1 + u*(b2-b1)
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    denom = dx1 * dy2 - dy1 * dx2
    if denom == 0:
        return None  # parallel (no overlap guaranteed)
    ex, ey = x3 - x1, y3 - y1
    t_num = ex * dy2 - ey * dx2
    u_num = ex * dy1 - ey * dx1
    # t = t_num / denom, u = u_num / denom; both in [0,1]
    if denom > 0:
        if not (0 <= t_num <= denom and 0 <= u_num <= denom):
            return None
    else:
        if not (denom <= t_num <= 0 and denom <= u_num <= 0):
            return None
    t = Fraction(t_num, denom)
    px = Fraction(x1) + t * dx1
    py = Fraction(y1) + t * dy1
    return (px, py)

def main():
    data = sys.stdin.read().split()
    i = 0
    n = int(data[i]); i += 1
    m = int(data[i]); i += 1
    red = [int(x) for x in data[i:i+n]]; i += n
    blue = [int(x) for x in data[i:i+m]]; i += m
    rseg = build(red)
    bseg = build(blue)
    points = set()
    for r in rseg:
        for b in bseg:
            p = seg_intersect(r, b)
            if p is not None:
                points.add(p)
    print(len(points))

main()
