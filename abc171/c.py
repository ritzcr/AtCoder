N = int(input())
alphabet = [
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y"]
out = []
div = 28


while True:
    N, mod = divmod(N, 26)
    if mod == 0:
        N -= 1
    out.append(alphabet[mod])
    if N == 0:
        break
print("".join(reversed(out)))
