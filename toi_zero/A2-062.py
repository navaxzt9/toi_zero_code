s = input().lower()
out = []
for v in "aeiou":
    c = s.count(v)
    if c > 0:
        out.append(f"{v}: {c}")
print("\n".join(out))
