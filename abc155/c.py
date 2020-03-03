N = int(input())
L = []
D = {}
for _ in range(N):
    x = input()
    L.append(x)

for x in L:
    D[x] = 0
    
for x in L:
    D[x] += 1

SortD = sorted(D.items(), key=lambda x:x[1])
maxD = SortD[-1][1]
ans = []
for x in reversed(SortD):
    if x[1] == maxD:
        ans.append(x[0])
    else:
        break
for x in sorted(ans):
    print(x)
