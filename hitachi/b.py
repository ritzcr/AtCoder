A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

minSum = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int, input().split())
    nowsum = a[x - 1] + b[y - 1] - c
    if nowsum < minSum:
        minSum = nowsum
print(minSum)
