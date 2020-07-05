S = list(input())
count_a = S.count("a")
count_b = S.count("b")
count_c = S.count("c")

if max(count_a, count_b, count_c) == count_a:
    print("a")
elif max(count_a, count_b, count_c) == count_b:
    print("b")
else:
    print("c")
