import sys
data = sys.stdin.read().split()
male = female = 0
for tok in data:
    n = int(tok)
    if n < 0:
        break
    if n % 2 == 0: female += 1
    else: male += 1
print(f"{male} {female} {male+female}")
