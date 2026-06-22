import sys
data = sys.stdin.read().split()
n = int(data[0]); L = int(data[1])
intervals = []
for i in range(n):
    s = int(data[2 + 2*i]); t = int(data[3 + 2*i])
    intervals.append((s, t))
intervals.sort(key=lambda x: x[1])
count = 0
last_point = -1
for s, t in intervals:
    if last_point < s:
        count += 1
        last_point = t
print(count)
