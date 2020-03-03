N = int(input())
S, T = input().split()

text = ""
for i in range(N):
    text += S[i]
    text += T[i]
print(text)
