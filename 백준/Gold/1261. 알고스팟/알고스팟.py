import collections


M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = [[100000] * M for _ in range(N)]
ans[0][0] = 0

q = collections.deque([[0, 0]])
while q:
    x, y = q.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 0 and ans[x][y] < ans[nx][ny]:
                ans[nx][ny] = ans[x][y]
                q.append([nx, ny])
            elif arr[nx][ny] == 1 and ans[x][y] + 1 < ans[nx][ny]:
                ans[nx][ny] = ans[x][y] + 1
                q.append([nx, ny])
print(ans[-1][-1])