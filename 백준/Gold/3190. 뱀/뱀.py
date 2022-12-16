N = int(input())  # 보드 크기(N*N)
K = int(input())  # 사과의 수
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 2
L = int(input())  # 뱀의 방향 전환 수
change_direction = [input().split() for _ in range(L)]
change_idx = 0

x = y = 0  # 뱀의 위치(x, y)
arr[0][0] = 1  # 첫 위치(0, 0)
snakes = [[0, 0]]  # 뱀 길이 = 1
time = 0
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
while True:
    time += 1
    x, y = x + direction[d][0], y + direction[d][1]
    if 0 <= x < N and 0 <= y < N:
        if arr[x][y] == 2:
            arr[x][y] = 1
            snakes.append([x, y])
        elif arr[x][y] == 0:
            arr[x][y] = 1
            snakes.append([x, y])
            s_x, s_y = snakes.pop(0)
            arr[s_x][s_y] = 0
        elif arr[x][y] == 1:
            break
    else:
        break
    if change_idx < len(change_direction) and int(change_direction[change_idx][0]) == time:
        if change_direction[change_idx][1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        change_idx += 1

print(time)