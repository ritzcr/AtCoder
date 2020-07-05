X, N = map(int, input().split())
if N > 0:
    p = list(map(int, input().split()))

    move = 0
    while True:
        minus_check = X - move
        if minus_check not in p:
            print(minus_check)
            break

        pulus_check = X + move
        if pulus_check not in p:
            print(pulus_check)
            break

        move += 1
else:
    print(X)
