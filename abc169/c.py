from decimal import Decimal

a, b = input().split()
a_deci = Decimal(a)
b_deci = Decimal(b)

ans = (a_deci * b_deci) // 1
print(ans)
