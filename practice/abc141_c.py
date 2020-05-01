N, K, Q = map(int, input().split())
A = [int(input()) for i in range(Q)]
N_array = [K - Q] * N
for x in A:
    N_array[x - 1] += 1
for z in N_array:
    if z > 0:
        print("Yes")
    else:
        print("No")
