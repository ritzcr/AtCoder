S = list(input())
lenS = len(S)

patternA = []
patternB = []
countA = 0
countB = 0

for x in range(lenS):
    if x % 2 == 0:
        if S[x] == "0":
            countA += 1
        else:
            countB += 1
    else:
        if S[x] == "1":
            countA += 1
        else:
            countB += 1

if countA < countB:
    print(countA)
else:
    print(countB)
    