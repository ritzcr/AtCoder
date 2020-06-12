X = int(input())
maxBeki = 1
for b in range(1, X, 1):
    for p in range(2, X, 1):
        if b**p <= X:
            maxBeki = max(maxBeki, b ** p)
        else:
            break
print(maxBeki)
