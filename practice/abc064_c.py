N = int(input())
a = list(map(int, input().split()))

over_3200 = 0
colors = {}
for x in a:
    if 1 <= x and x <= 399:
        colors.setdefault("grey", 0)
        colors["grey"] += 1
    elif 400 <= x and x <= 799:
        colors.setdefault("brown", 0)
        colors["brown"] += 1
    elif 800 <= x and x <= 1199:
        colors.setdefault("green", 0)
        colors["green"] += 1
    elif 1200 <= x and x <= 1599:
        colors.setdefault("sky", 0)
        colors["sky"] += 1
    elif 1600 <= x and x <= 1999:
        colors.setdefault("blue", 0)
        colors["blue"] += 1
    elif 2000 <= x and x <= 2399:
        colors.setdefault("yellow", 0)
        colors["yellow"] += 1
    elif 2400 <= x and x <= 2799:
        colors.setdefault("orange", 0)
        colors["orange"] += 1
    elif 2800 <= x and x <= 3199:
        colors.setdefault("red", 0)
        colors["red"] += 1
    else:
        over_3200 += 1

print(max(1, len(colors)), len(colors) + over_3200)
