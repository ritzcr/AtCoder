N = int(input())
a = list(map(int, input().split()))
count = 1
broke = 0
suceed = False
while True:
    if count in a:
        suceed = True
        broke += a.index(count)
        a = a[a.index(count) + 1:]
        count += 1
    else:
        broke += len(a)
        break
if suceed:
    print(broke)
else:
    print(-1)
