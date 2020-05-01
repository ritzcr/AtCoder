A, B, C = map(int, input().split())
flag = False
count = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    halfA = A // 2
    halfB = B // 2
    halfC = C // 2

    if A == (halfB + halfC) and B == (halfA + halfC) and C == (halfA + halfB):
        flag = True
        break
    else:
        A = halfB + halfC
        B = halfA + halfC
        C = halfA + halfB
        count += 1
if flag:
    print(-1)
else:
    print(count)
