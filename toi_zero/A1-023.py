t = int(input()); u = input().strip()
if u in ("F","f"):
    if t <= 32: print("solid")
    elif t >= 212: print("gas")
    else: print("liquid")
else:
    if t <= 0: print("solid")
    elif t >= 100: print("gas")
    else: print("liquid")
