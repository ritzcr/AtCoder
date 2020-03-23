N = int(input())
s = [list(input()) for i in range(N)]
out = [["-1"] * N for i in range(N)]
for x in range(N):
    for y in range(N):
        out[x][y] = s[N-1-y][x]

for x in out:
    print("".join(x))
