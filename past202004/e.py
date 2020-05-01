N = int(input())
A = list(map(int, input().split()))
out = [""] * N
for x in range(N):
    count = 1
    now = x
    while True:
        if A[now] == x + 1:
            out[x] = str(count)
            break
        else:
            count += 1
            now = A[now] - 1
print(" ".join(out))
