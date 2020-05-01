S = input()
North = S.count("N")
South = S.count("S")
East = S.count("E")
West = S.count("W")
if ((North > 0 and South > 0) or (North == 0 and South == 0)) and ((East > 0 and West > 0) or (East == 0 and West == 0)):
    print("Yes")
else:
    print("No")
