H, A = map(int, input().split())
times, mod = divmod(H, A)
if mod != 0:
    times += 1
print(times)
