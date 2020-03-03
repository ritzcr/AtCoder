N = int(input())
S = list(input())
xmax = 0
now = 0
for i in range(N):
    if S[i] == "I":
        now += 1
    elif S[i] == "D":
        now -= 1
    if now > xmax:
        xmax = now
print(xmax)
