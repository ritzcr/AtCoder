N, X = map(int, input().split())
L = list(map(int, input().split()))

sumL = 0
count = 0

for x in range(len(L) + 1):
    if sumL <= X:
        count += 1
    if x != len(L):
        sumL += L[x]
print(count)
