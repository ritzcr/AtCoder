N, M = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
remain = N - sumA
if remain >= 0:
    print(remain)
else:
    print(-1)
