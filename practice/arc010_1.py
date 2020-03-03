N, M, A, B = map(int, input().split())
C = []
comp = True
minusDay = 0
for x in range(M):
    if N <= A:
        N += B
    c = int(input())
    N -= c
    if N < 0:
        minusDay = x+1
        comp=False
        break
if comp == True:
    print("complete")
else:
    print(minusDay)