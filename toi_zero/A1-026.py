nums = [int(input()) for _ in range(3)]
e = sum(1 for x in nums if x % 2 == 0)
print(f"even {e}")
print(f"odd {3 - e}")
