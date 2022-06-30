N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1
# print(arr) = [[1, 0, 0, 0], [0, 1, 1, 0], [1, 1, 0, 0]]

max_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            stack = [[i, j]]
            arr[i][j] = 0
            cnt = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                        stack.append([nx, ny])
                        arr[nx][ny] = 0
                        cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
print(max_cnt)