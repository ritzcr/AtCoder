N, M, Q = map(int, input().split())
s = [list(map(int, input().split())) for i in range(Q)]
score = [[False] * M for i in range(N)]
value = [N] * M

success_dict = {}

for x in s:
    if x[0] == 1:
        score_sum = 0
        for y in range(M):
            if score[x[1] - 1][y]:
                score_sum += value[y]
        print(score_sum)
    else:
        score[x[1] - 1][x[2] - 1] = True
        value[x[2] - 1] -= 1
