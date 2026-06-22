n = int(input())
scores = list(map(int, input().split()))
avg = sum(scores) / n
print(f"{avg:.1f}")
if all(s >= 50 for s in scores) and avg >= 60.0:
    print("PASS")
else:
    print("FAIL")
