import itertools
import numpy as np


N, M, X = map(int, input().split())
books = np.array([list(map(int, input().split())) for i in range(N)])
minsum = N * 10**5
count = 0
check_array = []
success_array = []
for x in range(1, N + 1, 1):
    combi_list = list(itertools.combinations(range(N), x))
    for y in combi_list:
        sum_array = [0] * (M + 1)
        for z in y:
            sum_array = sum_array + books[z]
        beyond_check = True
        for zz in range(len(sum_array) - 1):
            if sum_array[zz + 1] < X:
                beyond_check = False
                break
        if beyond_check:
            success_array.append(sum_array[0])

    lenlist = len(combi_list)
    count += lenlist
if len(success_array) > 0:
    print(min(success_array))
else:
    print(-1)
