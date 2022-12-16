N, M = map(int, input().split())  # 세로, 가로
r, c, d = map(int, input().split())  # 로봇 청소기 위치, 방향
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
while True:
    # 1번
    if arr[r][c] == 0:
        answer += 1
        arr[r][c] = -1
    # 2번
    for _ in range(4):
        if d == 0:
            d = 3
        else:
            d -= 1
        nx, ny = r + direction[d][0], c + direction[d][1]
        if arr[nx][ny] == 0:
            r, c = nx, ny
            break
    else:
        nx, ny = r - direction[d][0], c - direction[d][1]
        if arr[nx][ny] != 1:
            r, c = nx, ny
        else:
            break
print(answer)