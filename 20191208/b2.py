import Levenshtein
import math

s=input()

lenght = len(s) 

round=lambda x:(x*2+1)//2

error = []
s_front = s[0:int(lenght/2)] 
s_back = s[round(lenght/2):lenght]

print(round(lenght/2))

s_back_reverse = s_back[::-1]
print(s_front)
print(s_back)
print(s_back_reverse)

lev = Levenshtein.distance(s_front, s_back_reverse)

error.append(lev)
print(error)