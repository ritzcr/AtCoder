N, A, B, C = map(int, input().split())
S = [input() for i in range(N)]
add = []

flag = True

for x in range(len(S)):
    if S[x] == "AB":
        if A == 0 and B == 0:
            flag = False
            break
        if A == 0:
            A += 1
            B -= 1
            add.append("A")
        elif B == 0:
            B += 1
            A -= 1
            add.append("B")
        elif x + 1 < len(S) and A + B + C == 2 and S[x + 1] != "AB":
            if S[x + 1] == "AC":
                A += 1
                B -= 1
                add.append("A")
            else:
                B += 1
                A -= 1
                add.append("B")
        elif A < B:
            A += 1
            B -= 1
            add.append("A")
        else:
            B += 1
            A -= 1
            add.append("B")
    elif S[x] == "AC":
        if A == 0 and C == 0:
            flag = False
            break
        if A == 0:
            A += 1
            C -= 1
            add.append("A")
        elif C == 0:
            C += 1
            A -= 1
            add.append("C")
        elif x + 1 < len(S) and A + B + C == 2 and S[x + 1] != "AC":
            if S[x + 1] == "BC":
                C += 1
                A -= 1
                add.append("C")
            else:
                A += 1
                C -= 1
                add.append("A")
        elif A < C:
            A += 1
            C -= 1
            add.append("A")
        else:
            C += 1
            A -= 1
            add.append("C")
    else:
        if B == 0 and C == 0:
            flag = False
            break
        if B == 0:
            B += 1
            C -= 1
            add.append("B")
        elif C == 0:
            C += 1
            B -= 1
            add.append("C")
        elif x + 1 < len(S) and A + B + C == 2 and S[x + 1] != "BC":
            if S[x + 1] == "AB":
                B += 1
                C -= 1
                add.append("B")
            else:
                C += 1
                B -= 1
                add.append("C")
        elif B < C:
            B += 1
            C -= 1
            add.append("B")
        else:
            C += 1
            B -= 1
            add.append("C")

if flag is True and A >= 0 and B >= 0 and C >= 0:
    print("Yes")
    for y in add:
        print(y)
else:
    print("No")
