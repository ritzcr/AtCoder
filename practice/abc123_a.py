abcde = []
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
abcde.append(int(input()))
k = int(input())

if (max(abcde) - min(abcde)) <= k:
    print("Yay!")
else:
    print(":(")
