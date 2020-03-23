N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [-1] * N
for x in range(N):
    if x == 0:
        dp[0] = 0
    elif x == 1:
        dp[1] = abs(h[1] - h[0])
    else:
        sub = min(K, x)
        MinDP = 10**9
        for y in range(1, sub + 1, 1):
            tmpDP = abs(h[x] - h[x - y]) + dp[x - y]
            if MinDP > tmpDP:
                MinDP = tmpDP
        dp[x] = MinDP
print(dp[N - 1])
