N = int(input())
S = input()

output = ""

for char in list(S):
    ASCII = ord(char)
    num = ASCII - 65
    num = (num + N) % 26
    ASCII = num + 65
    output += chr(ASCII)

print(output)