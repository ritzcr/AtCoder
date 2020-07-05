S = input()
sumS = 0

# 1 count
one_dict = {'.': 0}
for x in range(len(S)):
    one_dict[S[x]] = 0
sumS += len(one_dict)

# 2 count
if len(S) >= 2:
    two_dict = {}
    for y in range(len(S) - 1):
        two_dict[S[y:y + 2]] = 0
    two_count_dict = {'..': 0}
    for yy in two_dict:
        two_new_word_1 = "".join([yy[0], "."])
        two_new_word_2 = "".join([".", yy[1]])

        two_count_dict[yy] = 0
        two_count_dict[two_new_word_1] = 0
        two_count_dict[two_new_word_2] = 0
    sumS += len(two_count_dict)

# 3 count
if len(S) >= 3:
    three_dict = {}
    for z in range(len(S) - 2):
        three_dict[S[z:z + 3]] = 0
    three_count_dict = {'...': 0}
    for zz in three_dict:
        three_new_word_1 = "".join([zz[0], zz[1], "."])
        three_new_word_2 = "".join([zz[0], ".", zz[2]])
        three_new_word_3 = "".join([".", zz[1], zz[2]])
        three_new_word_4 = "".join([zz[0], ".", "."])
        three_new_word_5 = "".join([".", zz[1], "."])
        three_new_word_6 = "".join([".", ".", zz[2]])

        three_count_dict[zz] = 0
        three_count_dict[three_new_word_1] = 0
        three_count_dict[three_new_word_2] = 0
        three_count_dict[three_new_word_3] = 0
        three_count_dict[three_new_word_4] = 0
        three_count_dict[three_new_word_5] = 0
        three_count_dict[three_new_word_6] = 0

    sumS += len(three_count_dict)

print(sumS)
