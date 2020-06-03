N = int(input())
W = list(map(int, input().split()))

sum_min = 10**10
for x in range(N):
    first = W[:x]
    second = W[x:]
    sum_min = min(sum_min, abs(sum(first) - sum(second)))
print(sum_min)
