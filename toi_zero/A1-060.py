r, h, g = map(float, input().split())
PI = 3.14
width = h + 2 * r
length = 2 * PI * r + g
print(f"{width:.2f} {length:.2f}")
