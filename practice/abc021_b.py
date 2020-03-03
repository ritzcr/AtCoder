N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

route = []
route.append(a)
for x in P:
    route.append(x)
route.append(b)
if len(set(route)) == K+2:
    print("YES")
else:
    print("NO")