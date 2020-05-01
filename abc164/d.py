S = input()

count = 0
mod_check = [0] * 2019
mod_check[0] = 1
check_S = 0
d = 1
for i in reversed(S):
    check_S += int(i) * d
    check_S %= 2019
    mod_check[check_S] += 1
    d *= 10
    d %= 2019
    count += 1
mod_match = 0
for x in mod_check:
    mod_match += x * (x - 1) // 2
print(mod_match)
