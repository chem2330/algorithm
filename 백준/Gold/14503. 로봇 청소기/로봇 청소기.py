N, M = map(int, input().split())  # 행렬 크기(N * M)
x, y, d = map(int, input().split())  # 로봇 청소기 위치(x, y), 방향
arr = [list(map(int, input().split())) for _ in range(N)]  # 빈칸 = 0/ 벽 = 1
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 0
while True:
    if arr[x][y] == 0:
        arr[x][y] = 2
        cnt += 1
    for i in range(4):
        d = (d - 1) % 4
        if arr[x + direction[d][0]][y + direction[d][1]] == 0:
            x, y = x + direction[d][0], y + direction[d][1]
            break
    else:
        if arr[x - direction[d][0]][y - direction[d][1]] != 1:
            x, y = x - direction[d][0], y - direction[d][1]
        else:
            break

print(cnt)