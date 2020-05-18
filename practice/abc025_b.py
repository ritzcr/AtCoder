N, A, B = map(int, input().split())
sd = [list(input().split()) for i in range(N)]

now = 0
for x in sd:
    s, d = x[0], int(x[1])
    if d < A:
        d = A
    elif d > B:
        d = B
    if s == "East":
        now += d
    else:
        now -= d
if now > 0:
    print("East", now)
elif now < 0:
    print("West", now * -1)
else:
    print(0)
