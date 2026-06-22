line = input().strip()
# parse x and k from line. x is integer, k is single non-digit char (last char)
# format: x and k stuck together (e.g., "5A", "10#")
i = 0
while i < len(line) and line[i].isdigit():
    i += 1
x = int(line[:i])
k = line[i:].strip().upper()

mid_low = (x - 1) // 2
mid_high = x // 2

def letter_at(d):
    if k == "#":
        return "#"
    pos = ord(k) - ord("A")
    direction = 1
    for _ in range(d):
        new_pos = pos + direction
        if new_pos > 25:
            direction = -1
            new_pos = pos - 1
        elif new_pos < 0:
            direction = 1
            new_pos = pos + 1
        pos = new_pos
    return chr(pos + ord("A"))

for r in range(x):
    if r <= mid_low:
        col_left = mid_low - r
        d = mid_low - r
    else:
        col_left = r - mid_high
        d = r - mid_high
    col_right = x - 1 - col_left
    ch = letter_at(d)
    row = ["-"] * x
    row[col_left] = ch
    row[col_right] = ch
    print("".join(row))
