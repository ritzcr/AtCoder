S = input()
S = S.replace(S[0],"")
if len(S) > 0:
    S = S.replace(S[0],"")
    if len(S) == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
