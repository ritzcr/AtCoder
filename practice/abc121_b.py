N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]

count = 0
for x in range(N):
    A_check = A[x]
    sumNum = 0
    for y in range(M):
        sumNum += A_check[y] * B[y]
    sumNum += C
    if sumNum > 0:
        count += 1
print(count)
