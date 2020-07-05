N = int(input())
# tasks = [list(map(int, input().split())) for _ in range(N)]
tasks = {}
for i in range(N):
    A, B = map(int, input().split())
    # tasks.update({"day": A, "point": B, "done": False})
    tasks[i] = {"day": A, "point": B, "done": False}
# print(tasks.values())

sort_task = sorted(tasks.values(), key=lambda x: x['day'])
# print(sort_task)
sum_point = 0
for x in range(N):
    # print("x:", x)
    for y in sort_task:
        max_point = 0
        max_index = 0
        # print(x)
        if y["day"] > x + 1:
            break
        else:
            if y["point"] >= max_point and y["done"] is False:
                max_point = y["point"]
            # print(y["day"])

    sum_point += max_point
print(sum_point)
# if
# for y in sort_task:

# out = [-1] * N
# complete = 0

# for x in range(N):
#     maxIndex = 0
#     maxTask = 0
#     for y in range(len(sort_task)):
#         if sort_task[y][0] <= x + 1:
#             if maxTask < sort_task[y][1]:
#                 maxIndex = y
#                 maxTask = sort_task[y][1]
#         else:
#             break
#     sort_task.pop(maxIndex)
#     complete += maxTask
#     out[x] = complete
# for z in out:
#     print(z)
