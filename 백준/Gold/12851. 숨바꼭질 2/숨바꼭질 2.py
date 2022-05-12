from collections import deque


S, E = map(int, input().split())  # 수빈이 위치, 동생 위치
visited = [0] * 100001

queue = deque([S])
cnt = 0
while queue:
    v = queue.popleft()  # 꼭 popleft로 해야함, 방문 횟수를 하나씩 올려가면서 진행해야하기 때문(즉 dfs로만 가능)
    if visited[E] != 0 and visited[v] > visited[E]:
        break
    if v == E:
        cnt += 1
    else:
        for nv in [v + 1, v * 2, v - 1]:
            # dfs이기 때문에 visited[nv] < visited[v] + 1의 경우는 나오지 않음
            if 0 <= nv <= 100000 and (visited[nv] == 0 or visited[nv] == visited[v] + 1):
                visited[nv] = visited[v] + 1
                queue.append(nv)

print(visited[E])
print(cnt)