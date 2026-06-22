la, na = input().split()
lb, nb = input().split()
match_letter = (la == lb)
match_number = (na == nb)
last2 = (na[-2:] == nb[-2:])
last3 = (na[-3:] == nb[-3:])
prizes = []
if match_letter and match_number:
    prizes.append(1000000)
if (not match_letter) and match_number:
    prizes.append(100000)
if match_letter and last3:
    prizes.append(2000)
if match_letter and last2:
    prizes.append(1000)
if (not match_letter) and last3:
    prizes.append(200)
if (not match_letter) and last2:
    prizes.append(100)
if match_letter and not match_number:
    prizes.append(20)
print(max(prizes) if prizes else 0)
