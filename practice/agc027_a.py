N, x = map(int, input().split())
a = list(map(int, input().split()))
sort_a = sorted(a)
count = 0
for y in range(len(sort_a)):
    if y != len(sort_a) - 1:
        if sort_a[y] <= x:
            x -= sort_a[y]
            count += 1
        else:
            break
    else:
        if sort_a[y] == x:
            count += 1

print(count)
