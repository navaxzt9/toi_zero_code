from collections import deque
q = int(input())
normal = deque()
emergency = deque()
out = []
for _ in range(q):
    parts = input().split()
    cmd = parts[0]
    if cmd == "ARRIVE":
        name = parts[1]; t = parts[2]
        if t == "emergency":
            emergency.append(name)
        else:
            normal.append(name)
    elif cmd == "TREAT":
        if emergency:
            emergency.popleft()
        elif normal:
            normal.popleft()
    else:  # SHOW
        all_q = list(emergency) + list(normal)
        out.append(" ".join(all_q) if all_q else "EMPTY")
print("\n".join(out))
