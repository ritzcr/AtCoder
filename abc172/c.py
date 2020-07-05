N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
maxNM = max(N, M) + 1
dp = [0] * maxNM
time = 0
count = 0
Acount = 0
Bcount = 0
Asum = 0
Bsum = 0

while time < K:


print(count)
