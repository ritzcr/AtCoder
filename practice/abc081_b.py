N = int(input())
A = list(map(int, input().split()))

count = 0
flag = False
while True:
    for x in range(N):
        if A[x] % 2 == 0:
            A[x] = A[x] / 2
        else:
            flag = True
    if flag:
        break
    count += 1
print(count)
