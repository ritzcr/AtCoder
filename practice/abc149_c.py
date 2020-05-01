X = int(input())


def is_prime(n):
    if n == 1:
        return False
    else:
        for x in range(2, int(n ** 0.5) + 1):
            if (n % x) == 0:
                return False
        return True


while True:
    if is_prime(X):
        print(X)
        exit()
    else:
        X += 1
