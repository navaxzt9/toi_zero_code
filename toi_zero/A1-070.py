n = int(input())
types = ["Plastic", "Can", "Glass"]
for _ in range(n):
    vals = list(map(float, input().split()))
    total = sum(vals)
    parts = [f"{total:.1f}"]
    if total > 50:
        parts.append("Overloaded")
    for v, t in zip(vals, types):
        if v > 20:
            parts.append(f"Check Type {t}")
    print(",".join(parts))
