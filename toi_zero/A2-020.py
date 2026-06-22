import sys
data = sys.stdin.read().split()
n = int(data[0])
send = [0] + [int(x) for x in data[1:n+1]]
visited = [False] * (n + 1)
best = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    j = i
    length = 0
    while not visited[j]:
        visited[j] = True
        j = send[j]
        length += 1
    if length > best:
        best = length
print(best)
