N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

results = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            stack = [[i, j]]
            arr[i][j] = 0
            total = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                        arr[nx][ny] = 0
                        total += 1
                        stack.append([nx, ny])
            results.append(total)

print(len(results))
for result in sorted(results):
    print(result)