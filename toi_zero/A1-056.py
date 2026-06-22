def parse(line):
    line = line.strip()
    parts = line.split()
    if len(parts) == 3:
        return [int(x) for x in parts]
    # no spaces - single digit each
    return [int(c) for c in line if c.isdigit() or c == '-']

def parse_line(line):
    line = line.strip()
    parts = line.split()
    if len(parts) == 3:
        return [int(x) for x in parts]
    # treat as 3 single digits
    return [int(c) for c in line]

p1 = parse_line(input())
p2 = parse_line(input())
d = sum((a-b)**2 for a,b in zip(p1,p2)) ** 0.5
print(f"{d:.2f}")
