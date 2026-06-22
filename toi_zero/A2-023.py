s = input().strip()
sl = s.lower()
n = len(s)
violation = -1
for i, c in enumerate(sl):
    if c == "r":
        if i + 1 >= n or sl[i+1] != "a":
            violation = i + 1 if i + 1 < n else i
            break
    elif c == "a":
        if i == 0 or sl[i-1] not in ("r", "a"):
            violation = i
            break
    elif c == "b":
        if i + 1 >= n or sl[i+1] not in ("i", "t"):
            violation = i + 1 if i + 1 < n else i
            break
    # i, t: always ok
if violation >= 0:
    print(f"no {violation}")
else:
    has_pure_marker = any(c in "rab" for c in sl)
    if not has_pure_marker:
        print(f"unknown {n}")
    else:
        max_a = 0
        cur = 0
        for c in sl:
            if c == "a":
                cur += 1
                if cur > max_a:
                    max_a = cur
            else:
                cur = 0
        print(f"yes {max_a}")
