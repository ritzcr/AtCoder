O = input()
E = input()
out = ""
for x in range(len(O)):
    out += O[x]
    if len(E) > x:
        out += E[x]
print(out)
