n = int(input()); a = int(input())
total = n * a
if total == 0:
    print("No teaching")
else:
    h, m = divmod(total, 60)
    if h and m: print(f"{h} hours {m} minutes")
    elif h: print(f"{h} hours")
    else: print(f"{m} minutes")
