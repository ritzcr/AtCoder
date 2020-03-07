import sys
input = sys.stdin.readline

A, B = map(int, input().split())
out = 0
if A > B:
    out += A
    A -= 1
else:
    out += B
    B -= 1
if A > B:
    out += A
    A -= 1
else:
    out += B
    B -= 1
print(out)
