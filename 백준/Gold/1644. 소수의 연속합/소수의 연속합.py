N = int(input())

if N == 1:
    print(0)
else:
    primary_nums = [1] * (N + 1)
    for i in range(2, int(N ** 0.5) + 1):
        if primary_nums[i]:
            for j in range(i * 2, N + 1, i):
                primary_nums[j] = 0
    primary_list = []
    for i in range(2, N + 1):
        if primary_nums[i]:
            primary_list.append(i)
    # print(primary_list) = [2, 3, 5, 7, 11, 13, 17, 19]

    cnt = 0
    start = 0
    end = -1
    ssum = primary_list[0]
    primary_count = len(primary_list)

    while True:
        if ssum == N:
            cnt += 1
            if start == primary_count - 1:
                break
            start += 1
            end += 1
            ssum += (primary_list[start] - primary_list[end])
        elif ssum > N:
            end += 1
            ssum -= primary_list[end]
        elif start < primary_count - 1:
            start += 1
            ssum += primary_list[start]
        else:
            break

    print(cnt)