from functools import reduce

def gcd_base(x,y):
    while y!=0:
        x,y = y,x%y
    return x

def gcd(num):
    return reduce(gcd_base,num)

def lcm_base(x,y):
    return (x * y) // gcd_base(x,y)

def lcm(num):
    return reduce(lcm_base,num,1)

def calc_denom(l,numer):
    cnt = 0
    for x in l:
        cnt += numer//x
    return cnt

N = int(input())
l = list(map(int,input().split()))
numer = lcm(l)
denom = calc_denom(l,numer)
print(numer/denom)