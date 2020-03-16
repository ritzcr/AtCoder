N = int(input())
count = 1
while True:
    if count <= N:
        count = count * 2
    else:
        break
print(count // 2)
