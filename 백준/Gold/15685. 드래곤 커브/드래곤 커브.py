N = int(input())  # 드래곤 커브 개수
arr = [[0] * 101 for _ in range(101)]
direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    n_x, n_y = x + direction[d][0], y + direction[d][1]
    tmp = [[x, y], [n_x, n_y]]
    arr[x][y] = arr[n_x][n_y] = 1
    for _ in range(g):
        x, y = tmp[-1][0], tmp[-1][1]
        for i in range(len(tmp)-2, -1, -1):
            dx, dy = x - tmp[i][0], y - tmp[i][1]
            nx, ny = x + dy, y - dx
            tmp.append([nx, ny])
            arr[nx][ny] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1]:
            ans += 1
print(ans)