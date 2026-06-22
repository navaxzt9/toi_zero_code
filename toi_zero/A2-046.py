import sys
t = int(input())
out = []
for k in range(1, t + 1):
    s = input()
    sl = s.lower()
    vowels = sum(1 for c in sl if c in "aeiou")
    max_run = 0
    cur = 0
    for c in sl:
        if c in "aeiou":
            cur += 1
            if cur > max_run:
                max_run = cur
        else:
            cur = 0
    out.append(f"Line {k}: vowels = {vowels}, max_consecutive = {max_run}")
print("\n".join(out))
