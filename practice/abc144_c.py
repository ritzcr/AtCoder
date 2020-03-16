import math
N = int(input())
sqrtN = math.sqrt(N)
floorN = math.floor(sqrtN)
for x in range(floorN, 0, -1):
    if N % x == 0:
        y = N // x
        print(x + y - 2)
        break
