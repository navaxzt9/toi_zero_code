n = int(input())
roman = ["I","II","III","IV","V","VI","VII","VIII","IX"]
if n < 0:
    print("Error : Please input positive number")
elif 1 <= n <= 9:
    print(roman[n-1])
else:
    print("Error : Out of range")
