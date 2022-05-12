from collections import deque



S, E = map(int, input().split())  # 수빈이 위치, 동생 위치
visited = [0] * 100001

queue = deque([S])
cnt = 0
while queue:
    v = queue.popleft()
    if v == E:
        cnt += 1
    else:
        for nv in [v + 1, v * 2, v - 1]:
            if 0 <= nv <= 100000 and (visited[nv] == 0 or visited[nv] == visited[v] + 1):
                visited[nv] = visited[v] + 1
                queue.append(nv)

print(visited[E])
print(cnt)