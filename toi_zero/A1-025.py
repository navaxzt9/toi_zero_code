s = input().strip().upper()
rank, suit = s[:-1], s[-1]
ranks = {"A":"ace","J":"jack","Q":"queen","K":"king"}
suits = {"D":"diamonds","H":"hearts","S":"spades","C":"clubs"}
r = ranks.get(rank, rank).lower()
print(f"{r} of {suits[suit]}")
