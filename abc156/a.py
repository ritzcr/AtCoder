N,R = map(int,input().split())

if N <= 10:
    R = R + (10 - N) * 100
    
print(R)