H, W = map(int, input().split())
X = []
for _ in range(H):
    X.append(input())

print("#" * (W + 2))
for x in X:
    print("#", x, "#", sep="")    
print("#"*(W+2))