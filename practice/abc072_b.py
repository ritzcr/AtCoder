s = input()
out = ""
for x in range(len(s)):
    if x % 2 == 0:
        out += s[x]
print(out)
