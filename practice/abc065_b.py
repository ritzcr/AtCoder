N = int(input())
a = [int(input()) for i in range(N)]

now = 0
count = 0
checked = [-1] * N

while checked[now] == -1 and now != 1:
    checked[now] = 1
    now = a[now] - 1
    count += 1
if now == 1:
    print(count)
else:
    print(-1)
