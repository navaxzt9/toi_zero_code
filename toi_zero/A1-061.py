r, x, y = map(int, input().split())
d2 = x*x + y*y
r2 = r*r
if d2 < r2: print("IN")
elif d2 == r2: print("ON")
else: print("OUT")
