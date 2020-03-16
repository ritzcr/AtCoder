import math
a, b = map(str, input().split())
c = int(a + b)

d = math.sqrt(c)
div, mod = divmod(d, 1)
if mod == 0:
    print("Yes")
else:
    print("No")
