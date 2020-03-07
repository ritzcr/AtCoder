import sys
input = sys.stdin.readline

N = int(input())
S = list(str(N))
NumList = list(map(int, S))
sumNL = sum(NumList)

if N % sumNL == 0:
    print("Yes")
else:
    print("No")
