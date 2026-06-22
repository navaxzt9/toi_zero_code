import sys
MOD = (1 << 15) + 9
data = sys.stdin.read().split()
A = [[int(data[i*3 + j]) for j in range(3)] for i in range(3)]
B = [[int(data[9 + i*3 + j]) for j in range(3)] for i in range(3)]
C = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        s = 0
        for k in range(3):
            s += A[i][k] * B[k][j]
        C[i][j] = s % MOD
        if C[i][j] < 0:
            C[i][j] += MOD
for row in C:
    print(" ".join(map(str, row)))
