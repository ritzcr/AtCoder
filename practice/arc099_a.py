N, K = map(int, input().split())
A = list(map(int, input().split()))

minA = min(A)
indexA = A.index(minA)
print(minA)
print(indexA)
