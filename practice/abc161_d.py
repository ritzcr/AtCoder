from collections import deque

K = int(input())
d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
pop = 0
now = 0
while K > pop:
    now = d.popleft()
    if now % 10 != 0:
        d.append(now * 10 + (now % 10 - 1))
    d.append(now * 10 + (now % 10))
    if now % 10 != 9:
        d.append(now * 10 + (now % 10 + 1))
    pop += 1
print(now)
