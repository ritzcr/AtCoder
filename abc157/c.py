N, M = map(int, input().split())

answer = []
for x in range(N):
    answer.append(-1)

failCheck = False
for x in range(M):
    s, c = map(int, input().split())
    if answer[s - 1] == -1 or answer[s - 1] == c:
        answer[s - 1] = c
    else:
        failCheck = True
    if s == 1 and c == 0 and N > 1:
        failCheck = True

if failCheck:
    print(-1)
else:
    for x in range(len(answer)):
        if answer[x] == -1:
            if N == 1:
                answer[0] = 0
            elif x == 0:
                answer[x] = 1
            else:
                answer[x] = 0
    str_answer = map(str, answer)
    print("".join(str_answer))
