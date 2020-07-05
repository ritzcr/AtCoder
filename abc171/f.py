
import math

K = int(input())
S = input()
limit = 10**9 + 7

lenS = len(S)
allP = 26**(lenS + K)
removeP = 25**(lenS + K)
print((allP - removeP) % limit)

