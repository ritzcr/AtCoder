N = int(input())
a = sorted(map(int, input().split()), reverse=True)
sumA = 0
for x in range(len(a)):

    if x % 2 == 0:
        sumA += a[x]
    else:
        sumA -= a[x]
print(sumA)
