m = int(input()) / 1000
if m < 0.1:
    print("00")
elif m <= 5.0:
    print(str(int(m * 10)).zfill(2))
elif m <= 30.0:
    print(int(m) + 50)
elif m <= 70.0:
    print(int(((m) - 30) // 5) + 80)
else:
    print("89")
