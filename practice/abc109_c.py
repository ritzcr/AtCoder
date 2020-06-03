import fractions

N, X = map(int, input().split())
a = list(map(int, input().split()))

gcd = 0

for x in range(N):
    gcd = fractions.gcd(abs(a[x] - X), gcd)
print(gcd)
