import sys
stock = {}
out = []
for line in sys.stdin:
    parts = line.split()
    if not parts:
        continue
    cmd = parts[0]
    if cmd == "ADD":
        name, qty = parts[1], int(parts[2])
        stock[name] = stock.get(name, 0) + qty
    elif cmd == "REMOVE":
        name, qty = parts[1], int(parts[2])
        cur = stock.get(name, 0)
        if qty > cur:
            out.append(f"Not enough stock for {name}")
            if name in stock:
                del stock[name]
        else:
            stock[name] = cur - qty
            if stock[name] == 0:
                del stock[name]
    elif cmd == "CHECK":
        low = sorted([n for n, q in stock.items() if q < 5])
        if low:
            out.extend(low)
        else:
            out.append("All stocks are sufficient")
    elif cmd == "REPORT":
        for n in sorted(stock.keys()):
            if stock[n] > 0:
                out.append(f"{n}: {stock[n]}")
    elif cmd == "END":
        break
print("\n".join(out))
