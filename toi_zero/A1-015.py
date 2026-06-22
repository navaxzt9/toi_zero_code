name = input().strip()
surname = input().strip()
age = input().strip()
if len(name) > 5 and len(surname) > 5:
    print(name[:2] + surname[-1] + age[-1])
else:
    print(name[0] + age + surname[-1])
