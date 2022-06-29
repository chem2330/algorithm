N, M, V = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점
nodes = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    nodes[x] += [y]
    nodes[y] += [x]
# print(nodes) = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

# DFS
stack = [V]
dfs_visited = []
while stack:
    v = stack.pop()
    if v not in dfs_visited:
        dfs_visited.append(v)
        stack.extend(sorted(nodes[v], reverse=True))
print(*dfs_visited)

# BFS
queue = [V]
dfs_visited = []
while queue:
    v = queue.pop(0)
    if v not in dfs_visited:
        dfs_visited.append(v)
        queue.extend(sorted(nodes[v]))
print(*dfs_visited)