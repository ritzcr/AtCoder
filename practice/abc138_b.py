N = int(input())
A = list(map(int, input().split()))
sum_inv = 0
for i in range(N):
    sum_inv += 1 / A[i]
print(1 / sum_inv)
