M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

start = []
cnt = M * N
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            start.append([i, j])
            cnt -= 1
        elif arr[i][j] == -1:
            cnt -= 1
queue = [start]
day = -1
while queue:
    tomato_day = queue.pop(0)
    day += 1
    tmp = []
    for tomato in tomato_day:
        x, y = tomato
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                cnt -= 1
                tmp.append([nx, ny])
    if tmp:
        queue.append(tmp)

if cnt == 0:
    print(day)

else:
    print(-1)