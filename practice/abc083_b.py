N, A, B = map(int, input().split())
sumS = 0
for x in range(1, N + 1, 1):
    count = 0
    S = str(x)
    for y in range(len(str(x))):
        count += int(S[y])
    if count >= A and count <= B:
        sumS += x
print(sumS)
