import itertools

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(Q)]

array = list(itertools.combinations_with_replacement(range(1, M + 1), N))

maxScore = 0
for x in array:
    score = 0
    for y in abcd:
        if x[y[1] - 1] - x[y[0] - 1] == y[2]:
            score += y[3]
    maxScore = max(maxScore, score)
print(maxScore)
