A, B, K = map(int, input().split())
X = []

for x in range(K):
    if B >= A+x or B-x >= A:
        X.append(A+x)
        X.append(B-x)

sortX = sorted(set(X))
# print(" ".join(sortX))
for x in sortX:
    print(x)
