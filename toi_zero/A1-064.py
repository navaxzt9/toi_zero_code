import sys
data = sys.stdin.read()
# extract N and ops
i = 0
while i < len(data) and not data[i].isdigit():
    i += 1
j = i
while j < len(data) and data[j].isdigit():
    j += 1
n = int(data[i:j])
ops = [c for c in data[j:] if c in "+-"]
score = 0
for c in ops[:n]:
    if c == "+": score += 10
    else: score -= 5
print(score)
