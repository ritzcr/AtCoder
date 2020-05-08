N, M = map(int, input().split())
HFlag = [True] * N
H = list(map(int, input().split()))
ab = [list(map(int, input().split())) for i in range(M)]
for x in ab:
    if H[x[0] - 1] <= H[x[1] - 1]:
        HFlag[x[0] - 1] = False
    if H[x[0] - 1] >= H[x[1] - 1]:
        HFlag[x[1] - 1] = False
print(HFlag.count(True))
