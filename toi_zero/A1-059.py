routes = {
    ("BKK","CNX"): (10, 30),
    ("CNX","UBP"): (15, 40),
    ("UBP","BKK"): (20, 40),
    ("BKK","PKT"): (25, 50),
    ("PKT","CNX"): (30, 60),
    ("UBP","PKT"): (40, 70),
}
src, dst = input().split()
w = int(input())
key = (src, dst)
if key not in routes:
    print("Error")
else:
    fee, per = routes[key]
    print(fee + per * w)
