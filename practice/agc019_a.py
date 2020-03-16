Q, H, S, D = map(int, input().split())
N = int(input())

rate = {"Q": 4 * Q, "H": 2 * H, "S": S, "D": 1 / 2 * D}
price = 0
score_sorted = sorted(rate.items(), key=lambda x: x[1])
for x in score_sorted:
    if x[0] == "D" and N >= 2:
        div, mod = divmod(N, 2)
        N = mod
        price = D * div
    elif x[0] == "S":
        price += N * S
        break
    elif x[0] == "H":
        price += N * H * 2
        break
    elif x[0] == "Q":
        price += N * Q * 4
        break
    if N == 0:
        break
print(price)
