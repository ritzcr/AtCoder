N = int(input())
a = list(map(int, input().split()))

dictA = {}

for x in a:
    dictA.setdefault(x, 0)
    dictA[x] += 1
    if x - 1 > 0:
        dictA.setdefault(x - 1, 0)
        dictA[x - 1] += 1
    dictA.setdefault(x + 1, 0)
    dictA[x + 1] += 1
print(max(dictA.values()))
