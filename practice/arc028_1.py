N, A, B = map(int, input().split())

while True:
    N = N - A
    if N <= 0:
        print("Ant")
        break
    N = N - B
    if N <= 0:
        print("Bug")
        break
