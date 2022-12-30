N, M = map(int, input().split())
arr = []
cnt = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    cnt += sum(tmp)

ans = 0
while cnt > 0:
    ans += 1
    queue = [[0, 0]]
    visited = [[0] * M for _ in range(N)]
    melt = []
    while queue:
        x, y = queue.pop(0)
        visited[x][y] = 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny]:
                    cnt -= 1
                    melt.append([nx, ny])
                else:
                    queue.append([nx, ny])
    for x, y in melt:
        arr[x][y] = 0
print(ans)
print(len(melt))