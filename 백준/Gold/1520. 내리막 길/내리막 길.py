import sys


sys.setrecursionlimit(10 ** 6)


def street(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and arr[x][y] > arr[nx][ny]:
                dp[x][y] += street(nx, ny)
    return dp[x][y]


M, N = map(int, input().split())  # 세로 크기, 가로 크기
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

ans = 0
print(street(0, 0))