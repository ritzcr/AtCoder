X = int(input())
dp = [0] * (X + 1000)
dp[0] = 1
array = [100, 101, 102, 103, 104, 105]

for x in range(X):
    for y in array:
        if dp[x] == 1:
            dp[x + y] = 1
print(dp[X])
