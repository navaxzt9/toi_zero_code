x, y = map(int, input().split())
total = 0
count = 0
jump = x
while jump > 0 and total < y:
    total += jump
    count += 1
    jump -= 2
if total >= y:
    print(count)
else:
    print(-1)
