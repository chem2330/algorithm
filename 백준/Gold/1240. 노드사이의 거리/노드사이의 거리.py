import sys
import collections


input = sys.stdin.readline


def bfs(start, end):
    distances = [0] * (N + 1)
    queue = collections.deque([start])
    while queue:
        now = queue.popleft()
        for next, distance in nodes[now]:
            if next == end:
                return distances[now] + distance
            if distances[next] == 0:
                distances[next] = distances[now] + distance
                queue.append(next)

N, M = map(int, input().split())  # 노드의 수, 알고 싶은 노드쌍의 수

nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, r = map(int, input().split())
    nodes[a].append([b, r])
    nodes[b].append([a, r])

# 알고 싶은 노드
for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))