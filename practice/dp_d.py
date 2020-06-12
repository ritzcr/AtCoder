N, W = map(int, input().split())
bag = [list(map(int, input().split())) for i in range(N)]

dp = [-1] * (W + 1)
print(dp)

print(bag)
for x in range(W):
    if x == 0:
        dp[x] = 0
