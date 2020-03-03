N, K = map(int,input().split())
p = tuple(map(int,input().split()))
MaxSum = sum(p[:K])
tmp_SumSlice = MaxSum
for i in range(K, N):
    tmp_SumSlice = tmp_SumSlice + p[i] - p[i - K]
    if MaxSum < tmp_SumSlice:
        MaxSum = tmp_SumSlice
print((MaxSum+K)/2)