N, M = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353

dp = [[0 for i in range(M + 1)] for j in range(N)]
for n in range(N):
    for m in range(M + 1):
        print(A[n])
        if A[n] == m:
            dp[n][m] = max(dp[n - 1][m] + 1, dp[n - 1][m])
        else:
            dp[n][m] = max(dp[n - 1][m], dp[n - 1][m])
print(dp)
