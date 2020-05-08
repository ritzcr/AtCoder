X = int(input())
now = 100
count = 0
while now < X:
    now = now * 101 // 100
    count += 1
print(count)
