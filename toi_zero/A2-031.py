import sys
data = sys.stdin.read().split("\n")
idx = 0
n = int(data[idx].strip()); idx += 1
def parse_strand(line):
    parts = line.split()
    if len(parts) == n:
        return list(parts)
    return list(line.strip())
s1 = parse_strand(data[idx]); idx += 1
s2 = parse_strand(data[idx]); idx += 1
k = int(data[idx].strip()); idx += 1
for _ in range(k):
    parts = data[idx].split(); idx += 1
    strand = int(parts[0]); pos = int(parts[1]); new_g = parts[2]
    if strand == 1:
        s1[pos] = new_g
    else:
        s2[pos] = new_g
out1 = " ".join(s1)
out2 = " ".join(s2)
pair = {("A", "T"), ("T", "A"), ("C", "G"), ("G", "C")}
mismatch = sum(1 for a, b in zip(s1, s2) if (a, b) not in pair)
print(out1)
print(out2)
print(mismatch)
