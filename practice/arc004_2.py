N = int(input())
d = [int(input()) for i in range(N)]
print(sum(d))
print(max(0, 2 * max(d) - sum(d)))
