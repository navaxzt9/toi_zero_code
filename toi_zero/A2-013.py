p_kind, p_g = input().split()
t_kind, t_lvl, t_cc = input().split()
p_g = int(p_g); t_lvl = int(t_lvl); t_cc = int(t_cc)
pearl = {"H": 5, "O": 3, "J": 2}
tea = {
    "R": (12, 18, 25),
    "T": (15, 20, 30),
    "M": (10, 15, 20),
}
print(pearl[p_kind] * p_g + tea[t_kind][t_lvl - 1] * t_cc)
