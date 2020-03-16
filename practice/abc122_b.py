S = input()
maxS = 0
count = 0
for x in S:
    if x == "A" or x == "C" or x == "G" or x == "T":
        count += 1
    else:
        count = 0
    if maxS < count:
        maxS = count
print(maxS)
