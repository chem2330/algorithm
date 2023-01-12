import sys
import collections


input = sys.stdin.readline

N, Q = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())  # 동영상(p, r), usado(r)
    arr[p].append([q, r])  # 양방향 저장
    arr[q].append([p, r])


for _ in range(Q):
    ans = 0
    k, v = map(int, input().split())  # v동영상이랑 연결된 것 중에서 k이상인 동영상 찾기
    visited = [0] * (N + 1)
    visited[v] = 1
    queue = collections.deque([])
    queue.extend(arr[v])

    while queue:
        node, usado = queue.popleft()
        if not visited[node] and usado >= k:
            visited[node] = 1
            queue.extend(arr[node])
            ans += 1
    print(ans)
