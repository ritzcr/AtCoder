import itertools
abcd = list(map(int, input()))

case = ["+", "-"]
set_combination = list(itertools.product(case, repeat=3))

for x in set_combination:
    if x[0] == "+":
        sum_abcd = abcd[0] + abcd[1]
    else:
        sum_abcd = abcd[0] - abcd[1]
    if x[1] == "+":
        sum_abcd = sum_abcd + abcd[2]
    else:
        sum_abcd = sum_abcd - abcd[2]
    if x[2] == "+":
        sum_abcd = sum_abcd + abcd[3]
    else:
        sum_abcd = sum_abcd - abcd[3]

    if sum_abcd == 7:
        print("%d%s%d%s%d%s%d=7" % (abcd[0], x[0],
                                    abcd[1], x[1], abcd[2], x[2], abcd[3]))
        break
