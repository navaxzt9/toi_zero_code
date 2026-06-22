age = int(input()); status = input().strip()
print(20 if age < 18 or status in ("s", "S") else 50)
