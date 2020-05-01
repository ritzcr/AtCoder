S = input()

for x in range(len(S) - 2, 1, -2):
    sliceX = S[0:x]
    firstX = sliceX[0:(x // 2)]
    laterX = sliceX[(x // 2):]
    if firstX == laterX:
        print(len(sliceX))
        break
