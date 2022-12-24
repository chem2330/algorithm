arr = [[0]] + [list(map(int, input())) for _ in range(4)]
K = int(input())  # 회전 횟수
for _ in range(K):
    n, d = map(int, input().split())
    tmp = []
    tmp.append(arr[1][2])
    for i in range(2, 4):
        tmp.append(arr[i][6])
        tmp.append(arr[i][2])
    tmp.append(arr[4][6])
    if d == 1:
        arr[n] = arr[n][7:] + arr[n][:7]
    else:
        arr[n] = arr[n][1:] + arr[n][:1]
    for i in range(1, 4):
        now = n + i
        if now <= 4 and sum(tmp[now*2-4:now*2-2]) == 1:
            if ((n + now) % 2 and d == 1) or (not (n + now) % 2 and d == -1):
                arr[now] = arr[now][1:] + arr[now][:1]
            else:
                arr[now] = arr[now][7:] + arr[now][:7]
        else:
            break
    for i in range(-1, -4, -1):
        now = n + i
        if now >= 0 and sum(tmp[now*2-2:now*2]) == 1:
            if ((n + now) % 2 and d == 1) or (not (n + now) % 2 and d == -1):
                arr[now] = arr[now][1:] + arr[now][:1]
            else:
                arr[now] = arr[now][7:] + arr[now][:7]
        else:
            break
answer = 0
for i in range(1, 5):
    if arr[i][0]:
        answer += 2 ** (i - 1)
print(answer)