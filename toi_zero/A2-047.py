n = int(input())
out = []
for _ in range(n):
    s = input()
    sl = s.lower()
    tokens = sl.split()
    has_hello = any(t in ("hello", "hi") for t in tokens)
    has_bye = any(t in ("bye", "goodbye") for t in tokens)
    if has_hello:
        out.append("Hello! How can I help you?")
    elif has_bye:
        out.append("Goodbye! Have a nice day!")
    elif s.endswith("?"):
        out.append("That's an interesting question!")
    elif any(c.isdigit() for c in s):
        out.append("I see some numbers there!")
    elif sum(1 for c in s if not c.isspace()) > 19:
        out.append("That's quite a long message!")
    else:
        out.append("I understand.")
print("\n".join(out))
