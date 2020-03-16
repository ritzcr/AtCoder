N = int(input())
D, X = map(int, input().split())
# A = [int(input()) for i in range(N)]
for _ in range(N):
    y = int(input())
    div, mod = divmod(D, y)
    X += div
    if mod > 0:
        X += 1
print(X)
