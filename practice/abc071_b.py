S = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
A = list(alphabet)
for x in A:
    if x not in S:
        print(x)
        exit()
print("None")
