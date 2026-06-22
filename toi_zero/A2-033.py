def parse(s):
    parts = s.split(".")
    if len(parts) != 2:
        return None
    try:
        h = int(parts[0]); mm = int(parts[1])
    except ValueError:
        return None
    if not (0 <= h <= 23) or not (0 <= mm <= 59):
        return None
    return h * 60 + mm

a = input().strip()
b = input().strip()
ta = parse(a); tb = parse(b)
if ta is None or tb is None or ta >= tb:
    print("ERROR")
else:
    diff = tb - ta
    if diff < 15:
        print("FREE")
    else:
        hours = (diff + 59) // 60  # round up
        rates = {1: 25, 2: 50, 3: 80, 4: 110, 5: 145, 6: 180}
        if hours >= 7:
            print(250)
        else:
            print(rates[hours])
