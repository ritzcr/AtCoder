N = int(input())
S = input()

maxMatch = 0

for x in range(N):
    first_half = set(S[:x])
    second_half = set(S[x:])
    intersection = first_half & second_half
    maxMatch = max(maxMatch, len(intersection))
print(maxMatch)
