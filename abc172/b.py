S = input()
T = input()
count = 0
for x in range(len(S)):
    if S[x] != T[x]:
        count += 1
print(count)
