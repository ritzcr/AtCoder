S = input()
if S.count("hi") > 0:
    num = S.count("hi")
    S = S.replace("hi", "", num)
    if len(S) == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
