N = int(input())
A = list(map(int, input().split()))

rev_A = sorted(A, reverse=True)

if 0 in rev_A:
    print(0)
    exit()
else:
    limit = 10 ** 18
    current = 1

    for x in range(N):
        current *= rev_A[x]

        if current > limit:
            print(-1)
            exit()
    print(current)
