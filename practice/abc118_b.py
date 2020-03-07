N, M = map(int, input().split())

food = []
for x in range(N):
    ka = list(map(int, input().split()))
    a = ka[1:]
    if x == 0:
        food = a
    else:
        food = list(set(food) & set(a))
print(len(food))
