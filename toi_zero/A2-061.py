teams = ["CHE", "LIV", "MUN", "NEW"]
points = {t: 0 for t in teams}
pairs = []
for i in range(4):
    for j in range(i + 1, 4):
        pairs.append((teams[i], teams[j]))
for left, right in pairs:
    a, b = map(int, input().split())
    if a > b:
        points[left] += 3
    elif b > a:
        points[right] += 3
    else:
        points[left] += 1
        points[right] += 1
ranking = sorted(teams, key=lambda t: (-points[t], t))
for k, t in enumerate(ranking, 1):
    print(f"{k}. {t} {points[t]}")
