import sys
data = sys.stdin.buffer.read().split()
i = 0
n = int(data[i]); i += 1
cars = []
for _ in range(n):
    p = int(data[i]); i += 1
    v = int(data[i]); i += 1
    cars.append((p, v))
unsold = 0
suffix_max = 0
for j in range(n-1, -1, -1):
    if cars[j][1] < suffix_max:
        unsold += 1
    if cars[j][1] > suffix_max:
        suffix_max = cars[j][1]
print(unsold)
