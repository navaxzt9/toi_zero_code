s = input()
k = int(input())
print("".join(chr((ord(c) - ord('a') + k) % 26 + ord('a')) for c in s))
