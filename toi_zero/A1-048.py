n = int(input())
tiers = [(10, 5), (40, 7), (50, 10), (100, 12)]
units = n
cost = 0
for cap, rate in tiers:
    if units <= 0: break
    take = min(units, cap)
    cost += take * rate
    units -= take
if units > 0:
    cost += units * 15
ft = n * 0.50
vat = cost * 0.07
total = cost + ft + vat
print(f"{total:.2f}")
