N = int(input())
S = list(input())
out = ""
for x in range(N):
    if x == 0 or S[x] != S[x - 1]:
        out += S[x]

print(len(out))
