X, Y = map(int, input().split())
if X * 2 <= Y and X * 4 >= Y and Y % 2 == 0:
    print("Yes")
else:
    print("No")
