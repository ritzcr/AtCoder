from collections import Counter
N = int(input())
A = list(map(int, input().split()))
count = 0
l_array = []
r_array = []
for i, X in enumerate(A):
    l_array.append(i + X)
    r_array.append(i - X)

counter = Counter(r_array)

for x in l_array:
    count += counter.get(x, 0)
print(count)
