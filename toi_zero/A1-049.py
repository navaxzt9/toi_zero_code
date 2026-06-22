s = input().strip().zfill(5)
d = [int(c) for c in s]
if d[0] > 5: floor = 9
elif d[1] > 5: floor = 10
elif d[2] > 5: floor = 11
elif d[3] > 5: floor = 12
elif d[4] > 5: floor = 14
else: floor = 13

if s == s[::-1]:
    if d[0] + d[4] > 5: r1 = 1
    elif d[1] * d[3] > 5: r1 = 2
    else: r1 = 0
else:
    if d[4] != 0 and d[0] // d[4] > 5: r1 = 1
    elif d[1] - d[4] > 5: r1 = 2
    else: r1 = 0

s_sum = sum(d)
p = 1
for x in d: p *= x
if s_sum > 25: r2 = 1
elif p > 55: r2 = 2
else: r2 = 0

print(f"{floor}{r1}{r2}")
