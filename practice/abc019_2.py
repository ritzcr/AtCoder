S = input()
now = S[0]
count = 0
out_S = []
for x in S:
    if now != x:
        out_S.append(now)
        out_S.append(str(count))
        now = x
        count = 1
    else:
        count += 1
out_S.append(now)
out_S.append(str(count))
print("".join(out_S))
