S = input()
min_diff = 753
for i in range(len(S) - 2):
    compS = int(S[i : i + 3])
    comp = 753 - compS
    if comp < 0:
        comp = comp * -1
    if min_diff > comp:
        min_diff = comp
print(min_diff)
