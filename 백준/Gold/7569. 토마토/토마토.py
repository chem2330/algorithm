M, N, H = map(int, input().split())  # 가로, 세로, 높이

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

cnt = M * N * H
start = []

for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 1:
                start.append([z, x, y])
                cnt -= 1
            elif arr[z][x][y] == -1:
                cnt -= 1

day = -1
queue = [start]
while queue:
    tomato_daily = queue.pop(0)
    day += 1
    tmp = []
    for tomato in tomato_daily:
        z, x, y = tomato
        for dz, dx, dy in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nz, nx, ny = z + dz, x + dx ,y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = 1
                cnt -= 1
                tmp.append([nz, nx, ny])
    if tmp:
        queue.append(tmp)

if cnt:
    print(-1)
else:
    print(day)