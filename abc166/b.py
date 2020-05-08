N, K = map(int, input().split())
sunuke = [0] * N

for x in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for y in A:
        sunuke[y - 1] += 1
print(sunuke.count(0))
