m = int(input()); d = int(input())
base = {1:"winter",2:"winter",3:"winter",4:"spring",5:"spring",6:"spring",
        7:"summer",8:"summer",9:"summer",10:"fall",11:"fall",12:"fall"}
nxt = {"winter":"spring","spring":"summer","summer":"fall","fall":"winter"}
s = base[m]
if m % 3 == 0 and d >= 21:
    s = nxt[s]
print(s)
