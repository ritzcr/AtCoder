import itertools

X = int(input())

limit = 10 ** 13
check = [0]
now = 1
add = 1
while add < limit:
    add = now ** 5
    minus_add = add * -1
    check.append(add)
    check.append(minus_add)
    now += 1
new_array = sorted(check)
len_new_array = len(new_array)
check_combi = list(itertools.combinations(range(len(new_array)), 2))
for x in check_combi:
    if new_array[x[0]] - new_array[x[1]] == X:
        print(x[0] - (len_new_array - 1) // 2, x[1] - (len_new_array - 1) // 2)
        break
    if new_array[x[1]] - new_array[x[0]] == X:
        print(x[1] - (len_new_array - 1) // 2, x[0] - (len_new_array - 1) // 2)
        break
