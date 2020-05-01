N, A, B = map(int, input().split())
S = input()
for x in S:
    # print(x)
    if x == "a" and A + B > 0:
        if A > 0:
            A -= 1
            print("Yes")
        else:
            B -= 1
            print("Yes")
    elif x == "b" and A + B > 0 and B > 0:
        B -= 1
        print("Yes")
    else:
        print("No")
