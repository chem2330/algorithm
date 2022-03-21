T = int(input())
max_cnt = 0
for i in range(0, T + 1):
    j = 0
    arr = [T, i]
    cnt = 2
    while j >= 0:
        j = arr[-2] - arr[-1]
        cnt += 1
        arr += [j]
    if cnt >= max_cnt:
        max_cnt = cnt - 1
        max_arr = arr[0:-1]

print(max_cnt)
print(' '.join(map(str, max_arr)))
