n = int(input())
xs = [int(input()) for _ in range(n)]
print(sum(xs))
print(max(xs))
print(min(xs))
print(f"{sum(xs)/n:.1f}")
