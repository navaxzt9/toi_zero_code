n = int(input())
if n == 0:
    print("Student:")
    line2 = input() if False else ""
    print("Highest score: 0")
    print("Lowest score: 0")
    print("Average score: 0.0")
    print("Students who scored above average:")
else:
    scores = list(map(int, input().split()))
    names = [f"Student{i+1}" for i in range(n)]
    print("Student: " + " ".join(names))
    print(f"Highest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    avg = sum(scores) / n
    print(f"Average score: {avg:.1f}")
    print("Students who scored above average:")
    for i, s in enumerate(scores):
        if s > avg:
            print(f"Student {i+1}")
