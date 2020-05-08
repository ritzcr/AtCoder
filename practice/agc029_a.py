S = input()

sumB = 0
count = 0
for x in S:
    if x == "B":
        count += 1
    if x == "W":
        sumB += count
print(sumB)
