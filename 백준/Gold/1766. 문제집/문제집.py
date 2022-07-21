import sys
import heapq


input = sys.stdin.readline

N, M = map(int, input().split())  # 문제수, 정보수

arr = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

heap = []
answer = []

for _ in range(M):
    A, B = map(int, input().split())
    arr[A] += [B]
    degree[B] += 1
# print(arr) = [[], [], [], [1], [2]]
# print(degree) = [0, 1, 1, 0, 0]

for i in range(1, N + 1):
    if degree[i] == 0:
        heapq.heappush(heap, i)


while heap:
    now = heapq.heappop(heap)
    answer.append(now)
    for next in arr[now]:
        degree[next] -= 1
        if degree[next] == 0:
            heapq.heappush(heap, next)

print(*answer)