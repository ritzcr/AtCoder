Q = int(input())
queries = [list(input().split()) for i in range(Q)]
S = ""
# print(queries)
for q in queries:
    if q[0] == "1":
        input_str = str(q[1])
        S += input_str * int(q[2])
    else:
        slice_int = int(q[1])
        deleteS = S[:slice_int]
        S = S[slice_int:]
        delDict = {}
        for x in range(len(deleteS)):
            delDict[deleteS[x]] = 0
        for x in range(len(deleteS)):
            delDict[deleteS[x]] += 1
        delSum = 0
        for v in delDict.values():
            delSum += v**2
        print(delSum)
