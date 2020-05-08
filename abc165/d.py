A, B, N = map(int, input().split())

maxFloor = 0


def floor(x):
    num = int(x // 1)
    return num


if B - 1 <= N:
    check = floor(A * (B - 1) / B) - A * floor((B - 1) / B)
    print(check)
else:
    check = floor(A * N / B) - A * floor(N / B)
    print(check)


for x in range(N + 1):
    check = floor(A * x / B) - A * floor(x / B)
    # print("x:", x)
    # print("check:", check)
    if maxFloor <= check:
        maxFloor = check
        # print("max")
maxFloor = max(maxFloor, check)
print(maxFloor)
