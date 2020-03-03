N,K = map(int,input().split())

count=0
while True:
    N = N/K
    count += 1
    if N < 1:
        break
print(count)
