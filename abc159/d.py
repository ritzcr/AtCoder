N = int(input())
A = list(map(int, input().split()))
dictA = {}
for x in A:
    dictA[x] = 0
for x1 in A:
    dictA[x1] += 1

combisum = 0
for y in dictA.values():
    combisum += y * (y - 1) // 2

for z in range(N):
    print(combisum - dictA[A[z]] + 1)
