H, N = map(int, input().split())
A = map(int, input().split())

attack = sum(A)
if H <= attack:
    print("Yes")
else:
    print("No")
