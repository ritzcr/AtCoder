N = int(input())
S = [list(input()) for i in range(N)]

for x in range(N - 1, 0, -1):
    for y in range(len(S[x])):
        if S[x][y] == "X":
            # print(y)
            # print(len(S[x]) - )
            if y > 0:
                if S[x - 1][y - 1] == "#":
                    S[x - 1][y - 1] = "X"
            if S[x - 1][y] == "#":
                S[x - 1][y] = "X"
            if y < len(S[x]) - 1:
                if S[x - 1][y + 1] == "#":
                    S[x - 1][y + 1] = "X"

for z in range(N):
    print("".join(S[z]))
