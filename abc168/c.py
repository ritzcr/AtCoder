import math

A, B, H, M = map(int, input().split())
h = H * 30 + M / 2
m = M * 6
sita = min(abs(h - m), 360 - abs(h - m))
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(sita))))
