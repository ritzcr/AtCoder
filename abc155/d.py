import itertools

N,K = map(int,input().split())
A = sorted(map(int,input().split()))
D = []

for x in itertools.combinations(A, 2):
  D.append(x[0] * x[1])

X = sorted(D)
print(X[K-1])
