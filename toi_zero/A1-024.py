y = int(input()); cc = int(input())
if y <= 1990:
    rates = (1250, 1400, 2000)
elif y <= 1999:
    rates = (1100, 1300, 1700)
else:
    rates = (1000, 1200, 1500)
if cc <= 1500: print(rates[0])
elif cc <= 2000: print(rates[1])
else: print(rates[2])
