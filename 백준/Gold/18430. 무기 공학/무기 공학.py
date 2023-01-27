
def DFS(x, y, ssum):
    global mmax
    if ssum > mmax:
        mmax = ssum
    if not visited[x][y]:
        if x + 1 < N and y + 1 < M and not visited[x][y + 1] and not visited[x + 1][y + 1]:
            visited[x][y] = visited[x][y + 1] = visited[x + 1][y + 1] = 1
            ssum += arr[x][y] + arr[x][y + 1] * 2 + arr[x + 1][y + 1]
            if y + 1 < M:
                DFS(x, y + 1, ssum)
            elif x + 1 < N:
                DFS(x + 1, 0, ssum)
            visited[x][y] = visited[x][y + 1] = visited[x + 1][y + 1] = 0
            ssum -= arr[x][y] + arr[x][y + 1] * 2 + arr[x + 1][y + 1]
        if x + 1 < N and y - 1 >= 0 and not visited[x + 1][y - 1] and not visited[x + 1][y]:
            visited[x][y] = visited[x + 1][y - 1] = visited[x + 1][y] = 1
            ssum += arr[x][y] + arr[x + 1][y - 1] + arr[x + 1][y] * 2
            if y + 1 < M:
                DFS(x, y + 1, ssum)
            elif x + 1 < N:
                DFS(x + 1, 0, ssum)
            visited[x][y] = visited[x + 1][y - 1] = visited[x + 1][y] = 0
            ssum -= arr[x][y] + arr[x + 1][y - 1] + arr[x + 1][y] * 2
        if x + 1 < N and y + 1 < M and not visited[x + 1][y] and not visited[x + 1][y + 1]:
            visited[x][y] = visited[x + 1][y] = visited[x + 1][y + 1] = 1
            ssum += arr[x][y] + arr[x + 1][y] * 2 + arr[x + 1][y + 1]
            if y + 1 < M:
                DFS(x, y + 1, ssum)
            elif x + 1 < N:
                DFS(x + 1, 0, ssum)
            visited[x][y] = visited[x + 1][y] = visited[x + 1][y + 1] = 0
            ssum -= arr[x][y] + arr[x + 1][y] * 2 + arr[x + 1][y + 1]
        if x + 1 < N and y + 1 < M and not visited[x][y + 1] and not visited[x + 1][y]:
            visited[x][y] = visited[x][y + 1] = visited[x + 1][y] = 1
            ssum += arr[x][y] * 2 + arr[x][y + 1] + arr[x + 1][y]
            if y + 1 < M:
                DFS(x, y + 1, ssum)
            elif x + 1 < N:
                DFS(x + 1, 0, ssum)
            visited[x][y] = visited[x][y + 1] = visited[x + 1][y] = 0
            ssum -= arr[x][y] * 2 + arr[x][y + 1] + arr[x + 1][y]
    if y + 1 < M:
        DFS(x, y + 1, ssum)
    elif x + 1 < N:
        DFS(x + 1, 0, ssum)


N, M = map(int, input().split())  # 행렬(N * M)
arr = [list(map(int, input().split())) for _ in range(N)]
mmax = 0
visited = [[0] * M for _ in range(N)]
DFS(0, 0, 0)
print(mmax)
