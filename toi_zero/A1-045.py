n = int(input())
if n <= 1:
    fare = 35
elif n <= 10:
    fare = 35 + (n - 1) * 5
else:
    fare = 35 + 9 * 5 + (n - 10) * 8
print(fare)
