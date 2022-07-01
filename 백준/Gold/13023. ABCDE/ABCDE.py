def dfs(now, visited):
    global is_five_friends
    if len(visited) >= 5:
        is_five_friends = 1
        return
    for new in nodes[now]:
        if new not in visited:
            dfs(new, visited + [new])
    return


N, M = map(int, input().split())

nodes = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    nodes[a] += [b]
    nodes[b] += [a]
# print(nodes) = [[1], [0, 2], [1, 3], [2, 4], [3]]
is_five_friends = 0
for start in range(N):
    dfs(start, [start])
    if is_five_friends == 1:
        print(1)
        break
else:
    print(0)