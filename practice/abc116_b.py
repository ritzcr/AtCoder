s = int(input())
count = 1
A = [s]
while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = 3 * s + 1
    count += 1
    if s not in A:
        A.append(s)
    else:
        break
print(count)
