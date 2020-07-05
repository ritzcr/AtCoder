N = int(input())
a = list(map(int, input().split()))

xor_sum = 0
for x in a:
    xor_sum = x ^ xor_sum

for y in a:
    print(y ^ xor_sum)
