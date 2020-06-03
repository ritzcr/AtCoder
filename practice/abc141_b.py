S = input()
flag = True

for x in range(len(S)):
    if x % 2 == 0:
        if S[x] != "R" and S[x] != "U" and S[x] != "D":
            flag = False
            break
    else:
        if S[x] != "L" and S[x] != "U" and S[x] != "D":
            flag = False
            break
if flag:
    print("Yes")
else:
    print("No")
