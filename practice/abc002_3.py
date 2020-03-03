A = list(map(int, input().split()))

A[2] = A[2] - A[0]
A[3] = A[3] - A[1]
A[4] = A[4] - A[0]
A[5] = A[5] - A[1]
ad_bc = A[2] * A[5] - A[3] * A[4]
if ad_bc < 0:
    ad_bc = ad_bc * -1
print(ad_bc / 2)
