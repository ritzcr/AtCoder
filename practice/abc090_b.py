A, B = map(int, input().split())
count = 0
for x in range(A, B + 1, 1):
    letter = str(x)
    if letter[0] == letter[4] and letter[1] == letter[3]:
        count += 1
print(count)
