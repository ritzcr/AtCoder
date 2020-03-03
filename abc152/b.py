a,b = input().split()
out = ""
if a < b:
    tmp = b
    b = a
    a = tmp
for _ in range(int(a)):
    out += b
print(out)