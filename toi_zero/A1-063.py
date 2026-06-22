import sys
data = sys.stdin.read().split("\n")
T = int(data[0])
seats = T
out = []
for line in data[1:]:
    line = line.strip()
    if not line: continue
    parts = line.split()
    if len(parts) != 2: continue
    age = int(parts[0]); n = int(parts[1])
    if age < 15:
        out.append("-1")
        continue
    if n > seats:
        out.append("-2")
        continue
    if 15 <= age <= 22:
        price = int(150 * 0.8) * n
    elif age >= 60:
        price = int(150 * 0.5) * n
    else:
        price = 150 * n
    seats -= n
    out.append(f"{price} {seats}")
    if seats == 0:
        break
print("\n".join(out))
