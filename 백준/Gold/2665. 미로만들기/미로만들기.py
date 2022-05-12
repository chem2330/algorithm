n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
count_arr = [[n ** 2] * n for _ in range(n)]
count_arr[0][0] = 0
queue = [[0, 0]]
while queue:
    x, y = queue.pop(0)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                cnt = count_arr[x][y] + 1
            else:
                cnt = count_arr[x][y]
            if cnt < count_arr[nx][ny]:
                count_arr[nx][ny] = cnt
                queue.append([nx, ny])
print(count_arr[-1][-1])