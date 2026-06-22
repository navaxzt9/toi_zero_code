n = int(input())
xs = list(map(float, input().split()))
total = sum(xs)
avg = total / n
xs_sorted = sorted(xs)
if n % 2 == 1:
    median = xs_sorted[n // 2]
else:
    median = (xs_sorted[n // 2 - 1] + xs_sorted[n // 2]) / 2
mx = max(xs); mn = min(xs)
alert = sum(1 for x in xs if x >= 37)
print(f"SUM={total:.2f}")
print(f"AVG={avg:.2f}")
print(f"MEDIAN={median:.2f}")
print(f"MAX={mx:.2f}")
print(f"MIN={mn:.2f}")
print(f"ALERT={alert}")
print("SORTED=" + " ".join(f"{x:.2f}" for x in xs_sorted))
