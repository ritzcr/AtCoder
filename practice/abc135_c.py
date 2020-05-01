N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

kill = 0
for x in range(len(B)):
    next_town_kill = 0
    same_town_kill = min(B[x], A[x])
    kill += same_town_kill

    remain = B[x] - A[x]
    if remain > 0:
        next_town_kill = min(remain, A[x + 1])
        kill += next_town_kill
        A[x + 1] = max(A[x + 1] - remain, 0)
print(kill)
