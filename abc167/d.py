N, K = map(int, input().split())
A = list(map(int, input().split()))

flag = [False] * N
counted = [1]

nextT = A[0]
flag[0] = True
for x in range(N):
    if flag[nextT - 1] is False:
        counted.append(nextT)
        flag[nextT - 1] = True
        nextT = A[nextT - 1]
    else:
        break
before_loop_len = counted.index(nextT)
loop_len = x - before_loop_len + 1

if K <= before_loop_len:
    print(counted[K])
else:
    checkK_prep = K - before_loop_len
    checkK = checkK_prep % loop_len
    print(counted[before_loop_len + checkK])
