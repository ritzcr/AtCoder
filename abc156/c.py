N = int(input())
X = list(map(int,input().split()))
avex = round(sum(X)/N)
sumX = 0

for x in X:
    sumX = sumX + (x - avex) ** 2    
print(sumX)

