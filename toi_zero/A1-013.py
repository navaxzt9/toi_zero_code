c = input().strip()
d = input().strip()
ok_c = (c == "H")
ok_d = (d == "4567")
if ok_c and ok_d:
    print("safe unlocked")
elif ok_c:
    print("safe locked - change digit")
elif ok_d:
    print("safe locked - change char")
else:
    print("safe locked")
