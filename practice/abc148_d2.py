N = int(input())
a = list(map(int, input().split()))
count = 1
broke = 0

if 1 not in a:
    print(-1)
    exit()

for x in range(N):
    if a[x] == count:
        count += 1

print(N - count + 1)
