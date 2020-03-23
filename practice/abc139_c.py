N = int(input())
H = list(map(int, input().split()))
maxDown = 0
count = 0
for x in range(N-1):
    if H[x] >= H[x + 1]:
        count += 1
    else:
        count = 0
    if maxDown < count:
        maxDown = count
print(maxDown)
