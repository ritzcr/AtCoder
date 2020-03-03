N = int(input())
A = map(int,input().split())
lensetA = len(set(A))
if N == lensetA:
    print("YES")
else:
    print("NO")