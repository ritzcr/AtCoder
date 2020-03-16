import math

N = int(input())
for x in range(N, 0, -1):
    sq = math.sqrt(x)
    div, mod = divmod(sq, 1)
    if mod == 0:
        print(x)
        break
