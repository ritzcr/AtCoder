S = list(input())

flag = False

reverseS = list(reversed(S))
N = len(S)
firstN = (N - 1) // 2
laterN = (N + 3) // 2 - 1
first = S[0:firstN]
later = S[laterN: N + 1]
reverseFirst = list(reversed(first))
reverseLater = list(reversed(later))

if S == reverseS and reverseFirst == first and reverseLater == later:
    flag = True
if flag:
    print("Yes")
else:
    print("No")
