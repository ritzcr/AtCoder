from collections import deque


def main():
    geta = 250
    W = 500
    n, X, Y = map(int, input().split())
    X, Y = X + geta, Y + geta
    L = [list(map(int, input().split())) for _ in range(n)]
    obj = [[0] * W for _ in range(W)]
    for l in L:
        tmpx, tmpy = l[0] + geta, l[1] + geta
        obj[tmpx][tmpy] = 1
    que = deque()
    ans = 0
    que.append([geta, geta, 0])
    seen = [[0] * (W) for _ in range(W)]
    while(len(que) > 0):
        tmp = que.popleft()
        x = tmp[0]
        y = tmp[1]
        cnt = tmp[2]
        if x == X and y == Y:
            ans = cnt
            break
        move = [[1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [0, -1]]
        for m in move:
            nx, ny = x + m[0], y + m[1]
            try:
                if obj[nx][ny] == 0 and seen[nx][ny] == 0:
                    seen[nx][ny] = 1
                    que.append([nx, ny, cnt + 1])
            except BaseException:
                continue
    if seen[X][Y] == 1:
        print(ans)
    else:
        print(-1)


main()
