N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
closeH = {}
for x in range(len(H)):
    H[x] = T - H[x] * 0.006
    closeH[x + 1] = abs(A - H[x])
min_G = min(closeH, key=closeH.get)
print(min_G)
