A, R, N = map(int, input().split())
limit = 10 ** 9
limitFlag = False

sumA = A
for x in range(N - 1):
    sumA *= R
    if sumA > limit:
        limitFlag = True
        break
if limitFlag:
    print("large")
else:
    print(sumA)
