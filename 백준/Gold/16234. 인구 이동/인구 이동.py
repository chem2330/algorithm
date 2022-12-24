import copy
import collections


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    flag = 0
    arr2 = copy.deepcopy(arr)
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                queue = collections.deque()
                queue.append([i, j])
                tmp_pos = [[i, j]]
                tmp = arr[i][j]
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                            visited[nx][ny] = 1
                            queue.append([nx, ny])
                            tmp_pos.append([nx, ny])
                            tmp += arr[nx][ny]
                if len(tmp_pos) > 1:
                    flag = 1
                    change = tmp // len(tmp_pos)
                    for x, y in tmp_pos:
                        arr2[x][y] = change
    if flag:
        ans += 1
        arr = arr2
    else:
        break
print(ans)