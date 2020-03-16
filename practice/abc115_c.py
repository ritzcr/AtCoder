N, K = map(int, input().split())
h = [int(input()) for i in range(N)]
H = sorted(h)
# print(H)
minH = 10 ** 9
for x in range(N - K + 1):
    sumh = H[x + K - 1] - H[x]
    # print("sumh", sumh)
    if minH > sumh:
        minH = sumh
print(minH)
