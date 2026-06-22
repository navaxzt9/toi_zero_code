import sys
data = sys.stdin.read().split()
n = int(data[0])
rest = data[1:]
if len(rest) == 1 and len(rest[0]) == 2 * n:
    nums = [int(c) for c in rest[0]]
else:
    nums = [int(x) for x in rest]
maxes = [max(nums[2*i], nums[2*i+1]) for i in range(n)]
if n == 1:
    print(maxes[0])
else:
    print(" + ".join(str(x) for x in maxes) + f" = {sum(maxes)}")
