N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = [[0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud_list = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for _ in range(M - 1):
    d, s = map(int, input().split())  # 방향, 거리
    dx, dy = direction[d][0] * s, direction[d][1] * s
    move_cloud = [[(cloud[0] + dx) % N, (cloud[1] + dy) % N] for cloud in cloud_list]
    move_cloud_arr = [[0] * N for _ in range(N)]

    for cloud in move_cloud:
        arr[cloud[0]][cloud[1]] += 1
        move_cloud_arr[cloud[0]][cloud[1]] = 1
    for cloud in move_cloud:
        for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            nx, ny = cloud[0] + dx, cloud[1] + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
                arr[cloud[0]][cloud[1]] += 1

    cloud_list = []
    for i in range(N):
        for j in range(N):
            if move_cloud_arr[i][j] == 0 and arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud_list += [[i, j]]

d, s = map(int, input().split())  # 방향, 거리
dx, dy = direction[d][0] * s, direction[d][1] * s
move_cloud = [[(cloud[0] + dx) % N, (cloud[1] + dy) % N] for cloud in cloud_list]
move_cloud_arr = [[0] * N for _ in range(N)]

for cloud in move_cloud:
    arr[cloud[0]][cloud[1]] += 1
    move_cloud_arr[cloud[0]][cloud[1]] = 1
for cloud in move_cloud:
    for dx, dy in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
        nx, ny = cloud[0] + dx, cloud[1] + dy
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
            arr[cloud[0]][cloud[1]] += 1

total = 0
for i in range(N):
    total += sum(arr[i])
    for j in range(N):
        if move_cloud_arr[i][j] == 0 and arr[i][j] >= 2:
            total -= 2
print(total)