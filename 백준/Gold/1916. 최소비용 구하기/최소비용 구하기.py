import sys
import heapq


input = sys.stdin.readline

N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수
bus_list = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, l = map(int, input().split())
    bus_list[s].append([e, l])
start_position, end_position = map(int, input().split())

inf = N * 1000000
arr = [inf] * (N + 1)
arr[start_position] = 0

q = [(0, start_position)]

while q:
    total_cost, position = heapq.heappop(q)
    if total_cost <= arr[position]:
        for e, c in bus_list[position]:
            if arr[e] > total_cost + c:
                arr[e] = total_cost + c
                heapq.heappush(q, (total_cost + c, e))
                
print(arr[end_position])