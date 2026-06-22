import sys

def main():
    A, B = map(int, sys.stdin.readline().split())
    maxs = 3 * B + 2
    sieve = bytearray([1]) * maxs
    sieve[0] = sieve[1] = 0
    for i in range(2, int(maxs ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytes(len(sieve[i*i::i]))
    # prefix
    P = [0] * (maxs + 1)
    s = 0
    for i in range(maxs):
        s += sieve[i]
        P[i+1] = s
    count = 0
    Plocal = P
    for x in range(A, B+1):
        base_upper = x + B + 1
        base_lower = x
        sub = 0
        for y in range(x, B+1):
            sub += Plocal[base_upper + y] - Plocal[base_lower + 2*y]
        count += sub
    print(count)

main()
