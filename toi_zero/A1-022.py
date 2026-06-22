d = int(input()); m = int(input())
zodiac = [
    ((12,22),(1,19),"capricorn"),
    ((1,20),(2,18),"aquarius"),
    ((2,19),(3,20),"pisces"),
    ((3,21),(4,19),"aries"),
    ((4,20),(5,20),"taurus"),
    ((5,21),(6,21),"gemini"),
    ((6,22),(7,22),"cancer"),
    ((7,23),(8,22),"leo"),
    ((8,23),(9,22),"virgo"),
    ((9,23),(10,23),"libra"),
    ((10,24),(11,21),"scorpio"),
    ((11,22),(12,21),"sagittarius"),
]
for (sm,sd),(em,ed),name in zodiac:
    if sm <= em:
        if (m,d) >= (sm,sd) and (m,d) <= (em,ed):
            print(name); break
    else:
        if (m,d) >= (sm,sd) or (m,d) <= (em,ed):
            print(name); break
