import collections


N, M = map(int, input().split())  # 세로, 가로

arr = []  # 0은 길, 1은 벽
for _ in range(N):
    arr.append(list(map(int, input())))

inf = N * M * 2
visited = [[[inf, inf] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = visited[0][0][1] = 1


queue = collections.deque([[0, 0, 0]])
while queue:
    x, y, pre = queue.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0 and visited[nx][ny][pre] > visited[x][y][pre] + 1:
                visited[nx][ny][pre] = visited[x][y][pre] + 1
                queue.append([nx, ny, pre])
            elif arr[nx][ny] == 1 and pre == 0 and visited[nx][ny][1] > visited[x][y][0] + 1:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append([nx, ny, 1])
if min(visited[-1][-1]) == inf:
    print(-1)
else:
    print(min(visited[-1][-1]))