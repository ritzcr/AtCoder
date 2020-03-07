abcde = []
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))

minVal = 0
total = 0
for x in abcde:
    mod = x % 10
    if minVal == 0 and mod != 0:
        minVal = mod

    if minVal != 0 and mod != 0 and mod < minVal:
        minVal = mod

    if mod == 0:
        total += x - mod
    else:
        total += x + 10 - mod
if minVal != 0:
    total += minVal - 10
print(total)
