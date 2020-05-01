N, M = map(int, input().split())
dict = {}
for x in range(N):
    dict[x + 1] = 0
for y in range(M):
    a, b = map(int, input().split())
    dict[a] += 1
    dict[b] += 1
for z in dict.values():
    print(z)
