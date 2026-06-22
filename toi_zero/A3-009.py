import sys
data = sys.stdin.read().split()
n = int(data[0]); k = int(data[1])
arrivals = [0] * (k + 1)
for i in range(n):
    r = int(data[2 + i])
    arrivals[r] += 1
pods = min(arrivals[1:])
print(n - k * pods)
