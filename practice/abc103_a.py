A = sorted(map(int, input().split()))
sum = 0
for i in range(2):
    sum = sum + A[i + 1] - A[i]
print(sum)
