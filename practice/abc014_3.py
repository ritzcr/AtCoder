N = int(input())
ab = [list(map(int, input().split())) for i in range(N)]
enogu = [0] * (10**6 + 1)
for x in ab:
    enogu[x[0]] += 1
    if x[1] != 10**6:
        enogu[x[1] + 1] -= 1

current = 0
max_ab = 0
for y in enogu:
    current += y
    max_ab = max(max_ab, current)
print(max_ab)
