S = list(input())
out = []
for x in S:
    if x == "B":
        if len(out) != 0:
            out.pop(-1)
    else:
        out.append(x)
print("".join(out))
