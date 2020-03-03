S = list(input())
T = input()
match = False
for x in range(len(S)):
    rotate = S.pop()
    # rotate = S.(-1:)
    S.insert(0, rotate)
    moji = "".join(S)
    if moji == T:
        match = True

if match == True:
    print("Yes")
else:
    print("No")
