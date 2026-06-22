line1 = input().strip()
line2 = input().strip()
size, kind = line1[0], line1[1] if len(line1) >= 2 else line1.split()[1]
parts1 = line1.split()
if len(parts1) == 2:
    size, kind = parts1[0], parts1[1]
prices = {
    ("S","R"): 60, ("S","T"): 80,
    ("M","R"): 80, ("M","T"): 100,
    ("L","R"): 100, ("L","T"): 120,
}
total = prices[(size, kind)]
if line2 != "N":
    parts2 = line2.split()
    if len(parts2) == 2:
        topping, num = parts2[0], int(parts2[1])
    else:
        topping, num = line2[0], int(line2[1:])
    if topping == "P":
        total += 15 * num
    elif topping == "E":
        total += 10 * num
print(total)
