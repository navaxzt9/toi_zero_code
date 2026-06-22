import sys
lines = sys.stdin.read().split("\n")
n, m = map(int, lines[0].split())
img1 = [lines[1 + i] for i in range(n)]
img2 = [lines[1 + n + i] for i in range(n)]
rules = {
    ("-", "-"): "-",
    ("-", "+"): "+", ("+", "-"): "+",
    ("-", "x"): "x", ("x", "-"): "x",
    ("+", "x"): "*", ("x", "+"): "*",
    ("+", "+"): "+",
    ("x", "x"): "x",
}
out = []
for r in range(n):
    row = []
    for c in range(m):
        a = img1[r][c]; b = img2[r][c]
        row.append(rules.get((a, b), "-"))
    out.append("".join(row))
print("\n".join(out))
