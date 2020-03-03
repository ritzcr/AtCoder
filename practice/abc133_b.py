import math
import itertools

N,D= map(int,input().split())
X = []
count=0
for x in range(N):
    X.append(list(map(int,input().split()))) 

listArray = list(itertools.combinations(X, 2))

for X in listArray:
    sumX = 0
    for x in range(D):
        subX = X[0][x] - X[1][x]
        sumX += subX**2
     
    if math.sqrt(sumX).is_integer():
        count += 1
    
print(count)
