def bfs(x, y, d):
    global cnt
    if d > K:
        return
    if x == 0 and y == C - 1:
        if d == K:
            cnt += 1
        return
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and arr[nx][ny] != 'T':
            visited[nx][ny] = 1
            bfs(nx, ny, d + 1)
            visited[nx][ny] = 0
    return


R, C, K = map(int, input().split())  # 행렬의 크기(R * C),  목표 거리(K)
arr = [list(input()) for _ in range(R)]  # 현재 위치(왼쪽 아래), 집(오른쪽 위)
x, y = R - 1, 0  # 현재 위치
visited = [[0] * C for _ in range(R)]
visited[x][y] = 1
cnt = 0
bfs(x, y, 1)
print(cnt)