N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


count = 0

for x in range(N + 1):
    num_len = len(make_divisors(x))
    if x % 2 == 1 and num_len == 8:
        count += 1
print(count)
