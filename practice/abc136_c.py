N = int(input())
H = list(map(int, input().split()))

flag = True
minH = 0
for x in range(len(H)):
    if H[x] < minH:
        flag = False
        break
    else:
        if minH < H[x]:
            minH = H[x] - 1
if flag:
    print("Yes")
else:
    print("No")
