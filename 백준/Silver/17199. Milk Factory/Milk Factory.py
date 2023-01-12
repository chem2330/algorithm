N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)

ans = -1
visited = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    queue = arr[i][:]
    visited[i][i] = 1
    while queue:
        q = queue.pop(0)
        visited[i][q] = 1
        for k in arr[q]:
            if not visited[i][k]:
                queue.append(k)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if visited[j][i] == 0:
            break
    else:
        ans = i

print(ans)