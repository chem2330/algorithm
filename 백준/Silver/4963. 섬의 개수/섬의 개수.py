while True:
    w, h = map(int, input().split())  # 지도의 너비, 높이
    if (w, h) == (0, 0):
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                stack = [[i, j]]
                arr[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                            stack.append([nx, ny])
                            arr[nx][ny] = 0
    print(cnt)