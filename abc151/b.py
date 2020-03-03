n, k, m = map(int,input().split())
a = map(int, input().split())
current = 0
for x in a:
    current += x

last = n * m - current
if k < last:
    print(-1)
elif last < 0:
    print(0)
else:
    print(last)
