N, M, Q = map(int, input().split())
v = [list(map(int, input().split())) for i in range(M)]
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(Q)]
next_dict = {}
for x in range(M):
    next_dict.setdefault(v[x][0], []).append(v[x][1])
    next_dict.setdefault(v[x][1], []).append(v[x][0])

for y in s:
    print(c[y[1] - 1])
    if y[0] == 1:
        next_dict.setdefault(y[1], [])
        for z in next_dict[y[1]]:
            c[z - 1] = c[y[1] - 1]
    else:
        c[y[1] - 1] = y[2]
