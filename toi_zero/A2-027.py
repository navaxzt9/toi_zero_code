n = int(input())
scores = [int(input()) for _ in range(n)]
m = max(scores)
print(m)
print(scores.count(m))
