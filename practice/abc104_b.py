S = input()
flag1 = False
if S[0] == "A":
    S=S.replace("A","",1)
    if "C" in S[1:-1]:
        S = S.replace("C", "", 1)
        if S.islower():
            print("AC")
        else:
            print("WA")
    else:
            print("WA")
else:
            print("WA")