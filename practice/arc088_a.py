X, Y = map(int, input().split())
now = X
count = 0
while now <= Y:
    now = now * 2
    count += 1
print(count)
