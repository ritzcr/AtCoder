N = int(input())
S = input()

first = S[:N // 2]
second = S[N // 2:]

if first == second:
    print("Yes")
else:
    print("No")
