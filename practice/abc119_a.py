import datetime

S = input()
date = datetime.datetime.strptime(S, "%Y/%m/%d")
heisei = datetime.datetime.strptime("2019/04/30", "%Y/%m/%d")

if date <= heisei:
    print("Heisei")
else:
    print("TBD")
