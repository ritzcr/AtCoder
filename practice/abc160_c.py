K, N = map(int, input().split())
A = list(map(int, input().split()))
maxDis = 0
for x in range(len(A)):
    if x != len(A) - 1:
        maxDis = max(maxDis, A[x + 1] - A[x])
    else:
        maxDis = max(maxDis, A[0] - A[x] + K)
print(K - maxDis)
