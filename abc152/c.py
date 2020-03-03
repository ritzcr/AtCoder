n = int(input())
p = list(map(int,input().split())) 
count = 0
min = p[0]
for x in p:
    if x <= min :
        count += 1
        min = x
print(count)