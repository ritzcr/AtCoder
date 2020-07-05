N = int(input())
A = list(map(int, input().split()))
Q = int(input())

dictA = {}

for z in A:
    dictA.setdefault(z, 0)
    dictA[z] += 1

sumA = sum(A)

BC = [list(map(int, input().split())) for i in range(Q)]
for x in BC:
    if x[0] in dictA.keys():
        sumA += (x[1] - x[0]) * dictA[x[0]]
        dictA.setdefault(x[1], 0)
        dictA[x[1]] += dictA[x[0]]
        dictA.pop(x[0])
    print(sumA)
