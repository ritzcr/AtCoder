N = int(input())
S = ["".join(sorted(input())) for i in range(N)]

hashtable = {}

for x in S:
    hashtable.setdefault(x, 0)
    hashtable[x] += 1

sumS = 0
for y in hashtable.values():
    sumS += y * (y - 1) // 2
print(sumS)
