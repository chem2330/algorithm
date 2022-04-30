N = int(input())
big_list = []
for _ in range(N):
    x, y = map(int, input().split())
    big_list.append([x, y])
# print(big_list)
result = [0] * N
for i in range(N):
    now_x, now_y = big_list[i]
    cnt = 1
    for j in range(N):
        check_x, check_y = big_list[j]
        if now_x < check_x and now_y < check_y:
            cnt += 1
    result[i] = cnt
print(*result)