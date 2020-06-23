S = input()
choku_check = True
while True:
    if S[:2] == "ch":
        S = S[2:]
    elif S[:1] == "o":
        S = S[1:]
    elif S[:1] == "k":
        S = S[1:]
    elif S[:1] == "u":
        S = S[1:]
    elif S == "":
        break
    else:
        choku_check = False
        break
if choku_check:
    print("YES")
else:
    print("NO")
