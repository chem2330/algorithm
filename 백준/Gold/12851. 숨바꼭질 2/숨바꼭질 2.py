from collections import deque


S, E = map(int, input().split())  # 수빈이 위치, 동생 위치
visited = [0] * 100001

queue = deque([S])
cnt = 0
while queue:
    v = queue.popleft()  # 꼭 popleft로 해야함, 이동 횟수를 하나씩 올려가면서 진행해야하기 때문(즉 dfs로만 가능)
    if visited[E] != 0 and visited[v] > visited[E]:  # 최소 이동 횟수 초과하면 가지치기
        break
    if v == E:  # 도착지에 도착하면 다 cnt해줌
        cnt += 1
    else:  # 아직 도착지에 도착하지 않았으면 이동
        for nv in [v + 1, v * 2, v - 1]:
            # 범위 안에 들어오고, 방문하지 않았거나, 방문했던 장소라도 이동 횟수가 같으면 queue에 넣어줌
            # bfs이기 때문에 visited[nv] < visited[v] + 1의 경우는 나오지 않음
            if 0 <= nv <= 100000 and (visited[nv] == 0 or visited[nv] == visited[v] + 1):
                visited[nv] = visited[v] + 1
                queue.append(nv)

print(visited[E])
print(cnt)