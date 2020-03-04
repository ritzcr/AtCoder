import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = list(input())
S.pop(-1)

S[K - 1] = S[K - 1].lower()
print("".join(S))
