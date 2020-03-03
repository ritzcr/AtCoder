N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
B = sorted(set(A))
print(B[-2])