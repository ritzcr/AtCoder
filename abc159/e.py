H, W, K = map(int, input().split())
S = [list(input()) for i in range(H)]
for x in S:
    print(x.count("1"))
