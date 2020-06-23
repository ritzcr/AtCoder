N, Q = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(Q)]

osero = [0] * N
calc = [0] * N

for x in lr:
    calc[x[0] - 1] += 1
    if x[1] != N:
        calc[x[1]] -= 1
num = 0
for y in range(N):
    num += calc[y]
    if num % 2 == 1:
        osero[y] = 1

print("".join(map(str, osero)))
