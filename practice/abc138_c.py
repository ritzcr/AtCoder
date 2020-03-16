N = int(input())
v = sorted(map(int, input().split()))

material = v[0]
for x in range(N - 1):
    material = (material + v[x+1]) / 2
print(material)
