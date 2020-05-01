A, B, C = map(int, input().split())
array = [A, B, C]
count = 0
if (A % 2 == 1 and B % 2 == 0 and C % 2 == 0) or (A % 2 == 0 and B % 2 == 1 and C % 2 == 1):
    count += 1
    B += 1
    C += 1
elif (A % 2 == 0 and B % 2 == 1 and C % 2 == 0) or (A % 2 == 1 and B % 2 == 0 and C % 2 == 1):
    count += 1
    A += 1
    C += 1
elif (A % 2 == 0 and B % 2 == 0 and C % 2 == 1) or (A % 2 == 1 and B % 2 == 1 and C % 2 == 0):
    count += 1
    A += 1
    B += 1
if max(A, B, C) == A:
    count = count + (A - B) // 2 + (A - C) // 2
elif max(A, B, C) == B:
    count = count + (B - A) // 2 + (B - C) // 2
else:
    count = count + (C - A) // 2 + (C - B) // 2
print(count)
