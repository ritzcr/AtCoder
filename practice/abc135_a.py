A, B = map(int, input().split())

div, modAB = divmod(A + B, 2)
if modAB == 0:
    print(div)
else:
    print("IMPOSSIBLE")
