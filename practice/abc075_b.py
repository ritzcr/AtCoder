H, W = map(int, input().split())
a = [list(input()) for i in range(H)]

for h in range(H):
    for w in range(W):
        if a[h][w] == ".":
            count = 0
            x = [-1, 0, 1, -1, 1, -1, 0, 1]
            y = [-1, -1, -1, 0, 0, 1, 1, 1]
            if h > 0:
                if w > 0:
                    if a[h - 1][w - 1] == "#":
                        count += 1
                if a[h - 1][w] == "#":
                    count += 1
                if w < W - 1:
                    if a[h - 1][w + 1] == "#":
                        count += 1
            if w > 0:
                if a[h][w - 1] == "#":
                    count += 1
            if w < W - 1:
                if a[h][w + 1] == "#":
                    count += 1
            if h < H - 1:
                if w > 0:
                    if a[h + 1][w - 1] == "#":
                        count += 1
                if a[h + 1][w] == "#":
                    count += 1
                if w < W - 1:
                    if a[h + 1][w + 1] == "#":
                        count += 1
            a[h][w] = str(count)
for h2 in range(H):
    print("".join(a[h2]))
