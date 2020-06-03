N = int(input())
h = list(map(int, input().split()))
sumh = 0
maxH = max(h)
for x in range(maxH, 0, -1):
    print(x)
    sumh += h.count(maxH)
    h.index()

print(sumh)
