parts = input().split()
start = parts[0]
n = int(parts[1])
seq = ["Red", "Green", "Blue"]
m = {"R": 0, "G": 1, "B": 2}
i = m[start]
out = []
for k in range(n):
    out.append(seq[(i + k) % 3])
print(" ".join(out))
