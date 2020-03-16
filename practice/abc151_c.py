N, M = map(int, input().split())

AC = {}
WA = {}
PE = {}
for x in range(M):
    p, S = input().split()
    if S == "AC":
        AC[p] = {"AC"}
        if p in WA:
            PE[p] = WA[p]
    else:
        if p not in AC:
            if p not in WA:
                WA[p] = 1
            else:
                WA[p] += 1

print(len(AC), sum(PE.values()))
