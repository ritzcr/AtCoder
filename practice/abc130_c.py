W, H, x, y = map(int, input().split())

check = 0
if x * 2 == W and y * 2 == H:
    check = 1
print(W * H / 2, check)
