from decimal import Decimal, ROUND_HALF_UP
member = input().strip()
n = int(input())
total = Decimal("0")
for _ in range(n):
    total += Decimal(input().strip())
if member == "Y":
    final = total * Decimal("0.95")
elif total >= 500:
    final = total * Decimal("0.97")
else:
    final = total
print(final.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
