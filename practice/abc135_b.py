N = int(input())
p = list(map(int, input().split()))

check = []

for x in range(N):
    check.append(x + 1)

count = 0
for y in range(N):
    if check[y] != p[y]:
        count += 1

if count <= 2:
    print("YES")
else:
    print("NO")
