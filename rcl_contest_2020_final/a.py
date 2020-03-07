N, M = map(int, input().split())

dice = [1, 2, 3, 4, 5, 6]
dice[0] = 6
output = " ".join(map(str, dice))
print(output)
for _ in range(M):
    d, v, x = map(int, input().split())
    dice[1] = 6
    output = " ".join(map(str, dice))
    print(output)
