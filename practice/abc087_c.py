N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans1 = []
ans2 = []

for x in range(N):
    if x == 0:
        ans1.append(A1[x])
        ans2.append(A1[x] + A2[x])
    else:
        ans1.append(ans1[x - 1] + A1[x])
        ans2.append(max(ans1[x], ans2[x - 1]) + A2[x])
print(ans2[N - 1])
