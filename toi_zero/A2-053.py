name = input()
length = len(name)
first = ord(name[0].upper())
last = ord(name[-1].upper())
digits = []
for col in range(1, 11):
    v = col - 1
    if col % 2 == 1:
        x = first + v
    else:
        x = last - v
    x = x % length
    if x > 9:
        x = x % 10
    digits.append(x)
print(" ".join(str(d) for d in digits[2:8]))
