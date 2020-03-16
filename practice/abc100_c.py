N = int(input())
a = map(int, input().split())

count = 0
for x in a:
    while x % 2 == 0:
        count += 1
        x = x // 2

print(count)
