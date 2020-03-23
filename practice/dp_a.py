N = int(input())
h = list(map(int, input().split()))

dp = [-1] * N
for x in range(N):
    if x == 0:
        dp[0] = 0
    elif x == 1:
        dp[1] = abs(h[1] - h[0])
    else:
        dp[x] = min(abs(h[x] - h[x - 1]) + dp[x - 1],
                    abs(h[x] - h[x - 2]) + dp[x - 2])
print(dp[N - 1])
