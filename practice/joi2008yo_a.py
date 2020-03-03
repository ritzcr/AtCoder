S = int(input())
count = 0

returnS = 1000 - S
coin500, remain500 = divmod(returnS, 500)
coin100, remain100 = divmod(remain500, 100)
coin50, remain50 = divmod(remain100, 50)
coin10, remain10 = divmod(remain50, 10)
coin5, remain5 = divmod(remain10,5)
coin1, remain1 = divmod(remain5, 1)

count = coin500+coin100+coin50+coin10+coin5+coin1
print(count)