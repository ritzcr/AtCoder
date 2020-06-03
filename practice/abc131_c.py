import fractions

A, B, C, D = map(int, input().split())


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


LCM_CD = lcm(C, D)
C_Count = B // C - A // C
D_Count = B // D - A // D
CD_Count = B // (LCM_CD) - A // (LCM_CD)

print(C_Count, D_Count, CD_Count)
print(B - A + 1 - C_Count - D_Count + CD_Count)
