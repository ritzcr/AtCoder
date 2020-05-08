A, B, K = map(int, input().split())
remainK = K - A
A = A - K
if A < 0:
    A = 0
if remainK > 0:
    B = B - remainK
if B < 0:
    B = 0
print(A, B)
