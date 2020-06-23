S = list(input())
while "a" in S:
    S.remove("a")
while "e" in S:
    S.remove("e")
while "i" in S:
    S.remove("i")
while "o" in S:
    S.remove("o")
while "u" in S:
    S.remove("u")
print("".join(S))
