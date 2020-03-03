N = int(input())
A = map(int,input().split())

flag = True

for x in A:
    mod2 = x % 2
    if mod2 == 0:
        mod3 = x % 3
        mod5 = x % 5
        if mod3 != 0 and mod5 != 0:
            flag = False
if flag == True:
    print("APPROVED")
else:
    print("DENIED")