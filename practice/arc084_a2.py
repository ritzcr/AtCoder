from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))
sumSunuke = 0

for x in range(N):
    ab = bisect_left(A, B[x])
    bc = N - bisect_right(C, B[x])
    sumSunuke += ab * bc
print(sumSunuke)
