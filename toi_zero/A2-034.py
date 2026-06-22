n = int(input())
def is_prime(x):
    if x < 2: return False
    if x < 4: return True
    if x % 2 == 0: return False
    i = 3
    while i * i <= x:
        if x % i == 0: return False
        i += 2
    return True
if is_prime(n):
    print("Yes")
    primes = [str(p) for p in range(2, n + 1) if is_prime(p)]
    print(" ".join(primes))
else:
    print("No")
