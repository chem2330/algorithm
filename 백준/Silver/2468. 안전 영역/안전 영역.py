N = int(input())  # 행렬의 크기

arr = []
max_height = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    max_height = max(max(tmp), max_height)
# print(arr) = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
# print(max_height) = 9

max_cnt = 1
for water in range(1, max_height):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > water and visited[i][j] == 0:
                cnt += 1
                stack = [[i, j]]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > water and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            stack.append([nx, ny])
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)