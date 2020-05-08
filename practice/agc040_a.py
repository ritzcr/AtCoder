S = input()
previous = ""
count = 0
sumS = 0
for x in S:
    if previous == x:
        count += 1
    else:
        print(count)
        sumS += count * (count - 1) / 2
        count = 1
    previous = x
print(sumS)
