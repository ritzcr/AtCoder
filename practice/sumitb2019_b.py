N = int(input())
div = int(N / 1.08)
if int(int(div) * 1.08) == N:
    print(div)
elif int(int(div + 1) * 1.08) == N:
    print(div + 1)
else:
    print(":(")
