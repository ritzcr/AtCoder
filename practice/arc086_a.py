N, K = map(int, input().split())
A = list(map(int, input().split()))

dictCount = {}

for x in A:
    dictCount.setdefault(x, 0)
    dictCount[x] += 1
sorted_count = sorted(dictCount.items(), key=lambda x: x[1])
dict_len = len(sorted_count)
change_extract = sorted_count[:dict_len - K]
extract_sum = 0
for y in change_extract:
    extract_sum += y[1]
print(extract_sum)
