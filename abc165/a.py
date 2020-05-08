K = int(input())
A, B = map(int, input().split())
count = 1
check = 0
flag = False
while check < B:
    check = K * count
    if A <= check and check <= B:
        flag = True
    count += 1

if flag:
    print("OK")
else:
    print("NG")
