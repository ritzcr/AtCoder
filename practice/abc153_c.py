N, K = map(int, input().split())
H = sorted(map(int, input().split()))
if N < K:
    K = N
for _ in range(K):
    H.pop(-1)
print(sum(H))
