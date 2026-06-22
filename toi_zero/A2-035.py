import sys
data = sys.stdin.read().split()
n = int(data[0])
items = data[1:n+1]
results = []
def rec(used, cur):
    if len(cur) == n:
        results.append(" ".join(cur))
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            cur.append(items[i])
            rec(used, cur)
            cur.pop()
            used[i] = False
rec([False]*n, [])
print("\n".join(results))
print(len(results))
