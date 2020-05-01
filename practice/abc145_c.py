import itertools
import math

N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
all_pattern = math.factorial(N)
sum_length = 0
for i in itertools.permutations(range(N)):  # 0, 1, 2
    current_len = 0
    for x in range(len(i) - 1):
        sumlen = (xy[i[x + 1]][0] - xy[i[x]][0]) ** 2 + \
            (xy[i[x + 1]][1] - xy[i[x]][1]) ** 2
        current_len += math.sqrt(sumlen)
    sum_length += current_len
ave_length = sum_length / all_pattern
print(ave_length)
