A, B = map(int, input().split())
len = A - B * 2
if len < 0:
    len = 0
print(len)
