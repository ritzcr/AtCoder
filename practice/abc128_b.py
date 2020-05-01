N = int(input())
array = []
for x in range(N):
    S, P = input().split()
    array.append([x + 1, S, int(P)])
sort_array = sorted(array, key=lambda x: (x[1], -x[2]))

for y in sort_array:
    print(y[0])
