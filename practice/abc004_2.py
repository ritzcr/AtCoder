N = 4
c = [input().split() for i in range(N)]
z = [["?", "?", "?", "?"] for i in range(N)]
for x in range(4):
    for y in range(4):
        z[x][y] = c[3 - x][3 - y]
for x in z:
    print(" ".join(x))
