s, e = map(int, input().split())
primes = []
for n in range(max(s, 2), e + 1):
    if n < 2: continue
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False; break
        i += 1
    if is_prime:
        primes.append(n)
print(" ".join(str(p) for p in primes))
print(f"Total primes: {len(primes)}")
