def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != "X":
                tmp = int(maps[i][j])
                visited[i][j] = 1
                stack = [[i, j]]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                            tmp += int(maps[nx][ny])
                            visited[nx][ny] = 1
                            stack.append([nx, ny])
                answer.append(tmp)
    if answer:
        return sorted(answer)
    return [-1]