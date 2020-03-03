import itertools

N = int(input())
P = map(int,input().split())
Q = map(int, input().split())
listX = []
for x in range(N):
    listX.append(x+1)

tupleP = tuple(P)
tupleQ = tuple(Q)

per = itertools.permutations(listX)
count = 0
countP = 0
countQ = 0

for x in itertools.permutations(listX):
    if x == tupleP:
        countP=count
    if x == tupleQ:
        countQ=count
    count += 1

print(abs(countP-countQ))