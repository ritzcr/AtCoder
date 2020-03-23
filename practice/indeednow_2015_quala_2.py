N = int(input())
S = [sorted(input()) for i in range(N)]

k = sorted("indeednow")

for x in S:
    if x == k:
        print("YES")
    else:
        print("NO")
