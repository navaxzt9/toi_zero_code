tok = input().split()
if len(tok) == 1 and len(tok[0]) == 3:
    a, b, c = int(tok[0][0]), int(tok[0][1]), int(tok[0][2])
else:
    a, b, c = int(tok[0]), int(tok[1]), int(tok[2])
total = a*25 + b*40 + c*55
if a + b + c >= 3:
    total = int(total * 0.9)
print(total)
