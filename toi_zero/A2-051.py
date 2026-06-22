line1 = input().split()
n = int(line1[0]); m = int(line1[1])
if not (1 <= n <= 10) or not (1 <= m <= 20):
    print("Data Incorrect")
else:
    teams = []
    for _ in range(n):
        scores = list(map(int, input().split()))
        teams.append(scores)
    grand = 0
    out = []
    for i, t in enumerate(teams):
        avg = sum(t) / len(t)
        mx = max(t)
        out.append(f"Team {i+1}: Average = {avg:.2f}, Max = {mx}")
        grand += sum(t)
    out.append(f"Total Score of All Teams = {grand}")
    print("\n".join(out))
