from functools import lru_cache

N = int(input())

@lru_cache(maxsize=1000)
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(N))
