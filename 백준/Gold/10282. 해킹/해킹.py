import sys
import collections


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    arr = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())  # 단방향임
        arr[b].append([a, s])

    queue = collections.deque([[c, 0]])
    visited = [100000000] * (n + 1)
    last = c
    while queue:
        x, t = queue.popleft()
        if t < visited[x]:
            visited[x] = t
            last = x
            for n_x, n_t in arr[x]:
                queue.append([n_x, t + n_t])

    print(len(visited) - visited.count(100000000), end=' ')
    print(max(list(map(int, str(visited).replace('100000000', '-1')[1:-1].split(', ')))))