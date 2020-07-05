a = list(map(int, input().split()))
for x in range(len(a)):
    if a[x] == 0:
        print(x + 1)
        break
