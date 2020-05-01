N, M = map(int, input().split())
n_student = [list(map(int, input().split())) for i in range(N)]
m_point = [list(map(int, input().split())) for i in range(M)]

for x in range(N):
    min_y = 0
    min_value = 10**12
    for y in range(M):
        distance = abs(n_student[x][0] - m_point[y][0]) + \
            abs(n_student[x][1] - m_point[y][1])
        if distance < min_value:
            min_value = distance
            min_y = y + 1
    print(min_y)
