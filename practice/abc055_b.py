N = int(input())
power = 1
mod = 10 ** 9 + 7

for x in range(1, N + 1):
    power = power * x % mod
print(power)
