import itertools
L, R = map(int, input().split())

check = list(itertools.combinations(range(L, R + 1, 1), 2))

minmod = 2020
for x in check:
    minmod = min(minmod, (x[0] * x[1]) % 2019)

print(minmod)
