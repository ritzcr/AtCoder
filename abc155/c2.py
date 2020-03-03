import collections
import itertools

N = int(input())
L = []
D = {}
for _ in range(N):
    x = input()
    L.append(x)

counter = collections.Counter(L)

mode_v = counter.most_common()[0][-1]
it = itertools.takewhile(
    lambda kv: kv[-1] == mode_v, counter.most_common()
)
for k, v in it:
    print(k)