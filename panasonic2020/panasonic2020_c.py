a, b, c = map(int, input().split())
if a * b * 4 < (c - (a + b))**2 and c - (a + b) > 0:
    print("Yes")
else:
    print("No")
