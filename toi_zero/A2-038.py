n = int(input())
totF = totW = totE = 0
for _ in range(n):
    f1, w1, e1, f2, w2, e2 = map(int, input().split())
    s1 = f1 + w1 + e1
    s2 = f2 + w2 + e2
    if s1 >= s2:
        totF += f1; totW += w1; totE += e1
    else:
        totF += f2; totW += w2; totE += e2
total = totF + totW + totE
print(total)
print(f"{totF} {totW} {totE}")
print("YES" if totF > totW + totE else "NO")
