N = int(input())
T = list(map(int, input().split()))
M = int(input())
px = []
sumT = sum(T)
for _ in range(M):
    px.append(list(map(int, input().split())))

for x in px:
    sub = x[1] - T[x[0] - 1]
    newSum = sumT + sub
    print(newSum)
