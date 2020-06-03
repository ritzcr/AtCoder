s = input()
t = input()

s_check = sorted(s)
t_check = sorted(t, reverse=True)

if s_check < t_check:
    print("Yes")
else:
    print("No")
