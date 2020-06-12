N = int(input())
listA = [input() for i in range(N)]

dictA = {}

for y in listA:
    dictA.setdefault(y, 0)
    dictA[y] += 1
maxA = sorted(dictA.items(), key=lambda x: x[1], reverse=True)
print(maxA[0][0])
