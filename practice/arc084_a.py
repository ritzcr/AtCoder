N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
sumSunuke = 0


def bs_left(list, target):
    low, high = 0, len(list)
    while low < high:
        mid = (low + high) // 2
        if list[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def bs_right(list, target):
    low, high = 0, len(list)
    while low < high:
        mid = (low + high) // 2
        if list[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low


for x in range(N):
    ab = bs_left(A, B[x])
    bc = N - bs_right(C, B[x])
    print(ab)
    print(bc)
    sumSunuke += ab * bc
print(sumSunuke)
