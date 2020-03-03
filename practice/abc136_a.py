A, B, C = map(int, input().split())
remain = B + C - A
if remain < 0:
    remain = 0
print(remain)
