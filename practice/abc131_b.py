N, L = map(int, input().split())
array = []
minN = 10**10
for x in range(N):
    array.append(L + x)
    if abs(L + x) < abs(minN):
        minN = L + x
array.remove(minN)
print(sum(array))
