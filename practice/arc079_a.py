N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]
start = []
goal = []
flag = False
for x in range(M):
    if ab[x][0] == 1:
        start.append(ab[x][1])

    if ab[x][1] == N:
        goal.append(ab[x][0])

start_goal = set(start) & set(goal)

if start_goal:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
