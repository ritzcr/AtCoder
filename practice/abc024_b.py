N, T = map(int, input().split())
A = [int(input()) for i in range(N)]

sumA = T

for x in range(len(A) - 1):
    if (A[x + 1] - A[x]) < T:
        sumA += A[x + 1] - A[x]
    else:
        sumA += T
print(sumA)
