n = int(input())
a = map(int, input().split())

count = 0
for x in a:
    for y in range(x, 0, -1):
        if y % 2 == 0 or y % 3 == 2:
            count += 1
        else:
            break
print(count)