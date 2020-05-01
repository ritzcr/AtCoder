N = int(input())
B = list(map(int, input().split()))
A = [0] * N
for x in range(N - 1, -1, -1):
    if x == N - 1:
        A[x] = B[x - 1]
    elif x == 0:
        A[x] = B[x]
    else:
        A[x] = min(B[x], B[x - 1])
print(sum(A))
