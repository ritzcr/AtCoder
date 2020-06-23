N = input()
num = int(N)
sn = sum(map(int, list(N)))
if num % sn == 0:
    print("Yes")
else:
    print("No")
