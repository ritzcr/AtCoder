from copy import copy
N, K = map(int, input().split())
a = list(map(int, input().split()))
for x in range(K):
    b = [0] * N
    continue_Flag = False
    for y in range(N):
        for z in range(-1 * a[y], a[y] + 1, 1):
            if y + z >= 0 and y + z < N:
                b[y + z] += 1
        if a[y] != N:
            continue_Flag = True

    if not continue_Flag:
        break

    a = copy(b)
print(" ".join(map(str, a)))
