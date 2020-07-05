from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for x in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

prev = [-1] * (N + 1)
prev[0] = 0
prev[1] = 1


d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if prev[i] == -1:
            prev[i] = v
            d.append(i)

prev.pop(0)
prev.pop(0)
if len(prev) > 0:
    print("Yes")
    for y in prev:
        print(y)
else:
    print("No")
