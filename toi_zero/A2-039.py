nums = [int(input()) for _ in range(3)]
out = []
for i in range(3):
    out.append(f"Input number {i+1} stored.")
while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    cmd = int(line)
    if cmd == 0:
        break
    if cmd == 1:
        out.append("Original order: " + " ".join(map(str, nums)))
    elif cmd == 2:
        out.append("Descending order: " + " ".join(map(str, sorted(nums, reverse=True))))
    elif cmd == 3:
        out.append("Ascending order: " + " ".join(map(str, sorted(nums))))
print("\n".join(out))
