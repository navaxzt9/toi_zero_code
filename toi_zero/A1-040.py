cal = {1:100, 2:120, 3:200, 4:60}
total = 0
while True:
    x = int(input())
    if x == 5:
        break
    total += cal.get(x, 0)
print("Bye Bye")
print(f"Total Calories: {total}")
