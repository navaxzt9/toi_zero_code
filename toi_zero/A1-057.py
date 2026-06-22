g = int(input()); r = int(input())
if not (1 <= g <= 6 and 1 <= r <= 6):
    print("Invalid")
elif g == r:
    print("Correct!")
else:
    print("Wrong!")
