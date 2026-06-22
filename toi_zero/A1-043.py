base = int(input()); bonus = int(input()); days = int(input())
total = (base + bonus) * 1.5 if days > 3 else (base + bonus)
total = int(total) if total == int(total) else total
if total >= 1500: rank = 5
elif total >= 1000: rank = 4
elif total >= 500: rank = 3
elif total >= 200: rank = 2
else: rank = 1
if rank == 5 and days >= 7: special = 99
elif rank == 4 and bonus > 300: special = 88
else: special = 0
print(total)
print(rank)
print(special)
