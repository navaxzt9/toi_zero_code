n = int(input())
print("".join("X" if (i+1) % 5 == 0 else "*" for i in range(n)))
