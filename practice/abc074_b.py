N = int(input())
K = int(input())
x = list(map(int, input().split()))

sumX = 0
for y in x:
    if K / 2 < y:
        sumX += (K - y) * 2
    else:
        sumX += y * 2
print(sumX)
