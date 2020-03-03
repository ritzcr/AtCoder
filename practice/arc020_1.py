A, B = map(int, input().split())
if A < 0:
    A = A * -1
if B < 0:
    B = B * -1

if A < B:
    print("Ant")
elif A > B:
    print("Bug")
else:
    print("Draw")
