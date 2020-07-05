N, K = map(int, input().split())

mod = 10 ** 9 + 7

sumK = 0
for x in range(K, N + 1, 1):
    add = x * (2 * N - x + 1) / 2 - x / 2 * (x - 1)
    sumK = (sumK + add) % mod
print(sumK)
