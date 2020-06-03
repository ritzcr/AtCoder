S = list(input())

firstS = S[:len(S) // 2]
if len(S) % 2 == 0:
    secondS = list(reversed(S[len(S) // 2:]))
else:
    secondS = list(reversed(S[len(S) // 2 + 1:]))

count = 0

for x in range(len(firstS)):
    if firstS[x] != secondS[x]:
        count += 1
print(count)
