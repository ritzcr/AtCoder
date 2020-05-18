N, A, B = map(int, input().split())

if (N == 1 and A != B) or (B < A):
    print(0)
else:
    print((B - A) * (N - 2) + 1)
