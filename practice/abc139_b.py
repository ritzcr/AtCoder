A, B = map(int, input().split())

div, mod = divmod(B - A, A - 1)
div += 1
if mod > 0:
    div += 1
print(div)
