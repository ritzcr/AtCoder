N, M = map(int, input().split())
min_ID = 0
max_ID = N
for _ in range(M):
    L, R = map(int, input().split())
    if min_ID < L:
        min_ID = L
    if max_ID > R:
        max_ID = R

if max_ID < min_ID:
    print(0)
else:
    print(max_ID - min_ID + 1)

