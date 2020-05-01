N = int(input())
A = [int(input()) for i in range(N)]
maxA = max(A)
copy_A = A[:]
copy_A.remove(maxA)
secondA = max(copy_A)
for x in A:
    if x == maxA:
        print(secondA)
    else:
        print(maxA)
