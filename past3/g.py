from collections import deque

blocked = False

geta = 250
check_max = geta * 2

N, X, Y = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(N)]

d = deque([[geta, geta, 0]])
gold_move = [[1, 1], [-1, 1], [0, 1], [1, 0], [-1, 0], [0, -1]]

map = [[-1] * (check_max + 1) for i in range(check_max + 1)]

map[geta][geta] = 0
for z in xy:
    map[z[0] + geta][z[1] + geta] = -999

while True:
    check = d.popleft()
    # print(check)
    for move in gold_move:
        moved_X = check[0] + move[0]
        moved_Y = check[1] + move[1]
        if 0 <= moved_X and 0 <= moved_Y and check_max >= moved_X and check_max >= moved_Y:
            if map[moved_X][moved_Y] == -1:
                map[moved_X][moved_Y] = check[2] + 1
                d.append([moved_X, moved_Y, check[2] + 1])
        if map[X + geta][Y + geta] != -1:
            print(map[X + geta][Y + geta])
            exit()
    if not d:
        blocked = True
        break
print(-1)
