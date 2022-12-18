N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))
d_xy = [[0], [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [0] * 7

def turn(d):
    if d == 1:
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    elif d == 2:
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif d == 3:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    elif d == 4:
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]

for move in moves:
    nx, ny = x + d_xy[move][0], y + d_xy[move][1]
    if 0 <= nx < N and 0 <= ny < M:
        turn(move)
        x, y = nx, ny
        if arr[x][y]:
            dice[6] = arr[x][y]
            arr[x][y] = 0
            print(dice[1])
        else:
            arr[x][y] = dice[6]
            print(dice[1])