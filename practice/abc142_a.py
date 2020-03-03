N = int(input())
div, mod = divmod(N, 2)
if mod != 0:
    div += 1
oddness = div / N
print(oddness)
