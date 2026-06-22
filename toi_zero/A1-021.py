y = int(input())
leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) or (y < 1582 and y % 4 == 0)
print("yes" if leap else "no")
