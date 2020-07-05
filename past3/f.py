N = int(input())
a = [list(input()) for i in range(N)]

output = []
kaibun_bool = True

for x in range(N // 2):
    check_array_begin = a[x]
    check_array_end = a[N - x - 1]
    match = list(set(check_array_begin) & set(check_array_end))
    if match:
        output.append(match[0])
    else:
        kaibun_bool = False

if kaibun_bool:
    middle = ""
    if N % 2 == 1:
        middle = a[N // 2][0]
    output_string = "".join(output) + middle + "".join(reversed(output))
    print(output_string)

else:
    print(-1)
