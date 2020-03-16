N = int(input())
A = list(map(int, input().split()))
out = {}

for x in range(len(A)):
    out[x + 1] = A[x]

outlist = []
for k, v in sorted(out.items(), key=lambda x: x[1]):
    outlist.append(str(k))

print(" ".join(outlist))
