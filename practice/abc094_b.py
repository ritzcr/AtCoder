N, M, X = map(int, input().split())
A = list(map(int, input().split()))
lowerCount = 0
upperCount = 0
for y in A:
    if y > X:
        upperCount += 1
    else:
        lowerCount += 1
print(min(upperCount, lowerCount))
