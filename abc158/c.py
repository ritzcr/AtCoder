import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = 1
flag = False
for x in range(1300):
    if x // 12.5 == A and x // 10 == B:
        flag = True
        print(x)
        break

if not flag:
    print(-1)
