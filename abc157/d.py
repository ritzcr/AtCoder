import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


uf = UnionFind(N)

ab = []
for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a - 1, b - 1)
    ab.append([a, b])

out = []
for x in range(N):
    out.append(uf.size(x)-1)
    # print(uf.size(x))

for x in ab:
    out[x[0] - 1] -= 1
    out[x[1] - 1] -= 1

cd = []
for _ in range(K):
    c, d = map(int, input().split())
    if uf.same(c - 1, d - 1):
        out[c - 1] -= 1
        out[d - 1] -= 1
print(" ".join(map(str, out)))
