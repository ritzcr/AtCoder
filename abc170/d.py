from collections import Counter

N = int(input())
a = sorted(list(map(int, input().split())))

M = 10**6

table = [1] * (M + 1)

B = Counter(a)
Key = list(B.keys())

count = 0
for x in Key:
    if B[x] == 1 and table[x] == 1:
        count += 1

    for i in range(M):
        if i * x > M:
            break
        else:
            table[i * x] = 0

print(count)
