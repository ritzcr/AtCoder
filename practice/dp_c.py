N = int(input())
choice = [list(map(int, input().split())) for i in range(N)]
dp = [[-1] * (N), [-1] * (N), [-1] * (N)]
for x in range(N):
    if x == 0:
        dp[0][0] = choice[0][0]
        dp[1][0] = choice[0][1]
        dp[2][0] = choice[0][2]
    else:
        dp[0][x] = max(dp[1][x - 1], dp[2][x - 1]) + choice[x][0]
        dp[1][x] = max(dp[0][x - 1], dp[2][x - 1]) + choice[x][1]
        dp[2][x] = max(dp[0][x - 1], dp[1][x - 1]) + choice[x][2]
print(max(dp[0][-1], dp[1][-1], dp[2][-1]))
