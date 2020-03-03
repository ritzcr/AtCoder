A = []
out = []
for x in range(3):
    A.append(list(map(int, input().split())))
    out.append([0, 0, 0])
N = int(input())
b = []
for B in range(N):
    b.append(int(input()))
for pick in b:
    for y in range(3):
        for x in range(3):
            if pick == A[y][x]:
                out[y][x] = 1

bingo = False
for x in range(3):
    if out[x][0] == 1 and out[x][1] == 1 and out[x][2] == 1:
        bingo = True

for x in range(3):
    if out[0][x] == 1 and out[1][x] == 1 and out[2][x] == 1:
        bingo = True

for x in range(3):
    if out[0][0] == 1 and out[1][1] == 1 and out[2][2] == 1:
        bingo = True

    if out[2][0] == 1 and out[1][1] == 1 and out[2][0] == 1:
        bingo = True

if bingo:
    print("Yes")
else:
    print("No")
