import math

K = int(input())
sumGCD = K * K * K
for a in range(2, K + 1, 1):
    for b in range(2, K + 1, 1):
        for c in range(2, K + 1, 1):
            arr = [a, b, c]
            gcdNum = math.gcd(math.gcd(a, b), c)
            # if gcdNum != 1:
            # print(arr)
            # print(gcdNum)
            sumGCD += gcdNum - 1
print(sumGCD)
