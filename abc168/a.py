N = int(input())
mod = N % 10
if mod == 2 or mod == 4 or mod == 5 or mod == 7 or mod == 9:
    print("hon")
elif mod == 0 or mod == 1 or mod == 6 or mod == 8:
    print("pon")
else:
    print("bon")
