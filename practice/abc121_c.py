N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]

ab_hash = {}
count = 0
price_sum = 0
for x in range(len(ab)):
    ab_hash[x] = [ab[x][0], ab[x][1]]
ab_key_sorted = sorted(ab_hash.items(), key=lambda x: x[1][0])

for y in ab_key_sorted:
    if M > y[1][1]:
        price_sum += y[1][0] * y[1][1]
    else:
        price_sum += y[1][0] * M
    M -= y[1][1]
    if M <= 0:
        break

print(price_sum)
