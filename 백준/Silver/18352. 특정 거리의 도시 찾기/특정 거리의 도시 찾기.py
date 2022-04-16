from collections import deque

N, M, D, start = map(int, input().split())  # 도시 개수, 거리 개수, 거리, 시작 도시
node = dict()
for _ in range(M):
    A, M = map(int, input().split())
    if node.get(A):
        node[A] += [M]
    else:
        node[A] = [M]

visited = [-1] * (N + 1)
visited[start] = 0
queue = deque([start])
results = []
flag = 0
while queue:
    if flag == 1:
        break
    i = queue.popleft()
    if node.get(i):
        for j in node.get(i):
            if visited[j] == -1:
                visited[j] = visited[i] + 1
                if visited[j] == D:
                    results.append(j)
                if visited[j] > D:
                    flag = 1
                    break
                queue.append(j)

if results:
    for result in sorted(results):
        print(result)
else:
    print(-1)