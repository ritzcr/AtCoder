H, W = map(int, input().split())
bishop = W * H
if W == 1 or H == 1:
    print(1)
else:
    div, mod = divmod(bishop, 2)
    print(div + mod)
