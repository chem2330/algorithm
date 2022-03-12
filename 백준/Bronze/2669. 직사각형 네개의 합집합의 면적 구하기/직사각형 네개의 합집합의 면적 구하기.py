grid = [[0] * 100 for _ in range(100)]

for tc in range(4):
    x1, y1, x2, y2 = map(int, input().split())  # 1, 2, 4, 4
    for i in range(x2 - x1):  # [0, 1, 2]
        for j in range(y2 - y1):  # [0 ,1]
            grid[(x1 - 1) + i][(y1 - 1) + j] = 1

result = 0
for i2 in range(100):
    for j2 in range(100):
        if grid[i2][j2] == 1:
            result += 1

print(result)