N = int(input())
dict = {}
s = [input() for i in range(N)]
for x in range(N):
    dict[s[x]] = 0
for y in range(N):
    dict[s[y]] += 1
# print(dict)

M = int(input())
t = [input() for i in range(M)]
for z in range(M):
    if t[z] in dict:
        dict[t[z]] -= 1
if max(dict.values()) > 0:
    print(max(dict.values()))
else:
    print(0)
