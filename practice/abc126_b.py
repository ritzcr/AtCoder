S = input()
first = S[:2]
second = S[2:]
if 0 < int(first) and int(first) <= 12 and 0 < int(second) and int(second) <= 12:
    print("AMBIGUOUS")
elif 0 < int(second) and int(second) <= 12:
    print("YYMM")
elif 0 < int(first) and int(first) <= 12:
    print("MMYY")
else:
    print("NA")
