import sys
data = sys.stdin.read().split("\n")
n, d = map(int, data[0].split())
names = ["", "TechTrends", "EcoLife", "FoodieHeaven", "FashionWeek", "HealthyLiving"]
hashtags = []
for i in range(1, n + 1):
    parts = data[i].split()
    hid = int(parts[0])
    counts = list(map(int, parts[1:1+d]))
    hashtags.append((hid, counts))
out = []
best_total = -1
best_idx = -1
for i, (hid, c) in enumerate(hashtags):
    total = sum(c)
    avg = total / d
    if c[-1] > c[0]:
        trend = "GROWING"
    elif c[-1] < c[0]:
        trend = "DECLINING"
    else:
        trend = "STABLE"
    out.append(f"{names[hid]}: {total} total, {avg:.2f} avg, {trend}")
    if total > best_total:
        best_total = total
        best_idx = i
out.append(f"Top performer: {names[hashtags[best_idx][0]]}")
print("\n".join(out))
