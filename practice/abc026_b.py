import math

N = int(input())
r = [int(input()) for i in range(N)]
R = sorted(r, reverse=True)

sumR = 0
for x in range(len(R)):
    if x % 2 == 0:
        sumR += R[x] * R[x]
    else:
        sumR -= R[x] * R[x]
print(sumR * math.pi)
