from collections import deque

H, W = map(int, input().split())
c = [list(input()) for i in range(H)]
queue = deque()
checked = [[-1] * W for i in range(H)]
for i, x in enumerate(c):
    for j, y in enumerate(x):
        if y == "s":
            checked[i][j] == 1
            queue.append([i, j])

move = ([0, 1], [0, -1], [1, 0], [-1, 0])

ans = False
while len(queue):
    x = queue.pop()
    for d in move:
        dx = [x[0] + d[0], x[1] + d[1]]
        if dx[0] < 0 or dx[0] > H - 1 or dx[1] < 0 or dx[1] > W - 1:
            continue
        elif c[dx[0]][dx[1]] == "#":
            continue
        elif c[dx[0]][dx[1]] == "." and checked[dx[0]][dx[1]] == -1:
            checked[dx[0]][dx[1]] = 1
            queue.append((dx[0], dx[1]))
        elif c[dx[0]][dx[1]] == "g":
            ans = True
            break

if ans:
    print("Yes")
else:
    print("No")
