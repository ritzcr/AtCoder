import math

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]

maxA = 0
for x in range(N):
    for y in range(N):
        lenA = (A[x][0] - A[y][0]) ** 2 + (A[x][1] - A[y][1]) ** 2
        if lenA > maxA:
            maxA = lenA
print(math.sqrt(maxA))
