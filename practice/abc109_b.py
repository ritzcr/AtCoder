N = int(input())
past = []
last = ""
Success = True
for i in range(N):
    W = input()
    # print("past:", past)
    # print("W[0]:", W[0])
    # print("last[-1]:", last[-1:])
    if last == "":
        past.append(W)
        last = W
    elif W in past or W[0] != last[-1:]:
        Success = False
    else:
        past.append(W)
        last = W

if Success == True:
    print("Yes")
else:
    print("No")
