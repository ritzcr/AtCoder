N = int(input())
p = sorted([int(input()) for i in range(N)])
p[N - 1] = p[N - 1] // 2
print(sum(p))
