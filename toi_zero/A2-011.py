nums = list(map(int, input().split()))
seen = set()
out = []
for x in nums:
    if x not in seen:
        seen.add(x)
        out.append(str(x))
print(" ".join(out))
