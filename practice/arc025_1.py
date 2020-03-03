D = list(map(int, input().split()))
J = list(map(int, input().split()))
sumG = 0
for x in range(len(D)):
    if D[x] >= J[x]:
        sumG = sumG + D[x]
    else:
        sumG = sumG + J[x]
print(sumG)