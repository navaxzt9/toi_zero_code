parts = input().split()
pos = parts[0]; age = int(parts[1]); salary = int(parts[2])
base = {"M":1500, "B":1000, "G":500}
rates = {
    "M": (0.06, 0.08, 0.10),
    "B": (0.05, 0.06, 0.07),
    "G": (0.04, 0.05, 0.06),
}
if pos not in base:
    print(0)
else:
    if age < 5: r = rates[pos][0]
    elif age <= 10: r = rates[pos][1]
    else: r = rates[pos][2]
    print(int(base[pos] + salary * r))
