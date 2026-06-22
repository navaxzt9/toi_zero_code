nums = list(map(int, input().split()))
syms = ["#", "/", "+", "*"]
out = []
for n in nums:
    if n == 0:
        out.append("-")
        continue
    s = f"{n:04d}"
    part = ""
    for d, sym in zip(s, syms):
        if d != "0":
            part += sym
    out.append(part)
print("".join(out))
