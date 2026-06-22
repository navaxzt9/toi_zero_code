a = input().strip()
b = input().strip()
def pad(s, target):
    while len(s) < target:
        s += s[: target - len(s)] if (target - len(s)) <= len(s) else s
    return s[:target]
if len(a) < len(b):
    a = pad(a, len(b))
elif len(b) < len(a):
    b = pad(b, len(a))
love = set("love")
yant = []
for ca, cb in zip(a, b):
    if ca.lower() in love or cb.lower() in love:
        yant.append("w")
    else:
        yant.append("$")
s = "".join(yant)
cnt_w = s.count("w")
# find longest consecutive w run
max_run = 0
cur = 0
for c in s:
    if c == "w":
        cur += 1
        if cur > max_run:
            max_run = cur
    else:
        cur = 0
if cnt_w % 2 == 1:
    s += str(max_run)
else:
    if max_run < 2:
        s += "#"
print(s)
