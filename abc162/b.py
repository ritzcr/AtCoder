N = int(input())
sumN = 0
for x in range(N + 1):
    if x % 3 != 0 and x % 5 != 0:
        sumN += x
print(sumN)
