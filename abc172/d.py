import math
N = int(input())
sumN = 0
print(math.exp(N))

print(N**math.exp(N) - 1 // (N - 1))

# for x in range(1, N + 1, 1):
#     sumN += x * sympy.divisor_count(x)
# print(sumN)
