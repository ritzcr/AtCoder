N = int(input())
div, mod = divmod(N, 2)

if mod > 0:
    div = div + 1

print(div)
