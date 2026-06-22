s = input().strip()
sl = s.lower()
# Find max consecutive U/u immediately following any B/b
best = 0
for i, c in enumerate(sl):
    if c == "b":
        j = i + 1
        cnt = 0
        while j < len(sl) and sl[j] == "u":
            cnt += 1
            j += 1
        if cnt > best:
            best = cnt
if best >= 2:
    print(f"Yes {best}")
elif "b" in sl:
    idx = sl.index("b")
    print(s[: idx + 1] + "U" * (len(s) - idx - 1))
else:
    pat = "BUU"
    print((pat * ((len(s) // 3) + 1))[: len(s)])
