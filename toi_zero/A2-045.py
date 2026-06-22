import sys
data = sys.stdin.read().split()
i = 0
blocks = []
while i + 1 < len(data):
    prev = int(data[i]); h = int(data[i+1])
    blocks.append((prev, h))
    i += 2
    if h == 0:
        break
n = len(blocks)
out = []
if n == 1:
    print("1X")
else:
    for k in range(n - 1, 0, -1):
        # block k (1-indexed), check Prev[k+1] == Hash[k]
        prev_next = blocks[k][0]
        hash_cur = blocks[k - 1][1]
        ok = (prev_next == hash_cur)
        out.append(f"{k}{'P' if ok else 'X'}")
    print("\n".join(out))
