w = input()

hash = {}

for x in range(len(w)):
    hash[w[x]] = 0

for x in range(len(w)):
    hash[w[x]] += 1

beautiful = True
for v in hash.values():
    if v % 2 != 0:
        beautiful = False
if beautiful:
    print("Yes")
else:
    print("No")
