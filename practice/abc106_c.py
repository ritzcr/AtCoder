S = input()
K = int(input())

count = 0
while count < len(S):
    if S[count] == "1":
        count += 1
    else:
        break
if K > count:
    print(S[count])
else:
    print(1)
