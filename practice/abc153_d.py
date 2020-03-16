H = int(input())
count = 0
for x in range(H):
    if H < 2 ** count:
        break
    else:
        count += 1
print(2 ** count - 1)
