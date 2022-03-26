def pipe(x, y, direction):
    global cnt
    if (x, y) == (N - 1, N - 1):
        cnt += 1
        return
    if direction == 0 or direction == 2:
        if y + 1 < N and arr[x][y + 1] == 0:
            pipe(x, y + 1, 0)
    if direction == 1 or direction == 2:
        if x + 1 < N and arr[x + 1][y] == 0:
            pipe(x + 1, y, 1)
    if direction == 0 or direction == 1 or direction == 2:  # 대각선
        if x + 1 < N and y + 1 < N and arr[x][y + 1] == 0 and arr[x + 1][y + 1] == 0 and arr[x + 1][y] == 0:
            pipe(x + 1, y + 1, 2)
    return


N = int(input())  # 행렬의 크기(N * N)
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0  # 경로의 수(최종값)
pipe(0, 1, 0)  # 첫 파이프 위치
print(cnt)