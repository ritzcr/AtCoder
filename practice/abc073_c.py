N = int(input())
dictA = {}
for x in range(N):
    k = int(input())
    dictA.setdefault(k, 0)
    dictA[k] += 1
count = 0
for y in dictA.values():
    if y % 2 == 1:
        count += 1
print(count)
