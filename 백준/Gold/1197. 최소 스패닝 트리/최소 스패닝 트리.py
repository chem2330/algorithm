import sys
import heapq


input = sys.stdin.readline

V, E = map(int, input().split())
visited = [0] * (V + 1)
arr = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    arr[s].append([w, e])
    arr[e].append([w, s])
# print(arr) = [[], [[1, 2], [3, 3]], [[1, 1], [2, 3]], [[2, 2], [3, 1]]]

total = 0
cnt = 0
heap = [[0, 1]]
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = 1
        total += w
        cnt += 1
        for i in arr[s]:
            heapq.heappush(heap, i)
print(total)