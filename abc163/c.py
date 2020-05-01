N = int(input())
A = list(map(int, input().split()))
count_array = [0] * N
for x in range(N - 1):
    count_array[A[x] - 1] += 1
for y in count_array:
    print(y)
