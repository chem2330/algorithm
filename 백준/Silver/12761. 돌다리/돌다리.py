import collections


A, B, N, M = map(int, input().split())  # 콩콩의 힘(A, B) / 동규 위치(N) / 주미 위치(M)

inf = 100001
visited = [inf] * 100001
visited[N] = 0
queue = collections.deque([N])
while queue:
    q = queue.popleft()
    if q == M:
        break
    for i in [A, B]:
        if (q + i) <= 100000 and visited[q + i] > visited[q] + 1:
            visited[q + i] = visited[q] + 1
            queue.append(q + i)
        if 0 <= (q - i) and visited[q - i] > visited[q] + 1:
            visited[q - i] = visited[q] + 1
            queue.append(q - i)
        if (q * i) <= 100000 and visited[q * i] > visited[q] + 1:
            visited[q * i] = visited[q] + 1
            queue.append(q * i)
    if (q + 1) <= 100000 and visited[q + 1] > visited[q] + 1:
        visited[q + 1] = visited[q] + 1
        queue.append(q + 1)
    if 0 <= (q - 1) and visited[q - 1] > visited[q] + 1:
        visited[q - 1] = visited[q] + 1
        queue.append(q - 1)
print(visited[M])