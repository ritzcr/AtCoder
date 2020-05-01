S = list(input())
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    tmp = list(reversed(S[a-1:b]))
    count = 0
    for x in range(a - 1, b, 1):
        S[x] = tmp[count]
        count += 1
print("".join(S))
