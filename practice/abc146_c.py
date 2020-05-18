A, B, X = map(int, input().split())

small = 0
big = 10 ** 9
mid = big

while True:
    nowLen = len(str(mid))
    if mid == 0:
        nowLen = 0

    sumX = A * mid + B * nowLen
    nextsumX = A * (mid + 1) + B * len(str(mid + 1))
    if (sumX <= X and nextsumX > X) or(sumX <= X and mid == big):
        break
    elif X < sumX:
        big = mid
        mid = (small + big) // 2
    else:
        small = mid
        mid = (small + big) // 2

print(mid)
