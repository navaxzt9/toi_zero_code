N, K, T = map(int, input().split())
cur = 1
seen = {1}
count = 1
while True:
    cur = (cur - 1 + K) % N + 1
    if cur == 1:
        break
    count += 1
    if cur == T:
        break
print(count)
