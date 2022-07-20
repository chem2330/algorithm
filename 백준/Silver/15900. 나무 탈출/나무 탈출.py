import sys
import collections


input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr) = [[], [8, 4, 3], [3], [1, 2], [1, 7, 6], [6], [4, 5], [4], [1]]

cnt = 0
visited = [0] * (N + 1)
visited[1] = 1
queue = collections.deque([1])
while queue:
    v = queue.popleft()
    for i in arr[v]:
        if not visited[i]:
            visited[i] = visited[v] + 1
            queue.append(i)
        if len(arr[i]) == 1:
            cnt += visited[v]
            
# print(visited) = [0, 1, 3, 2, 2, 4, 3, 3, 2]

if cnt % 2:
    print('Yes')
else:
    print('No')