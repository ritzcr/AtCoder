N, Y = map(int, input().split())
flag = False
for x in range(N, -1, -1):
    for y in range(N - x, -1, -1):
        z = N - x - y
        if 10000 * x + 5000 * y + 1000 * z == Y:
            print(x, y, z)
            bool = True
            exit()

if not flag:
    print(-1, -1, -1)
