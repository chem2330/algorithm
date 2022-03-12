grid = [[0] * 100 for _ in range(100)]
T = int(input())
for tc in range(1, T + 1):
    x, y = list(map(int, input().split()))
    for i in range(10):
        for j in range(10):
            grid[x + i][y + j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            cnt += 1
print(cnt)