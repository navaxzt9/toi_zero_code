import sys
from collections import Counter
data = sys.stdin.read().split()
n = int(data[0])
sizes = list(map(int, data[1:n+1]))
print(max(Counter(sizes).values()))
