import sys
import heapq


input = sys.stdin.readline

N = int(input())

queue = [0] * N
for _ in range(N):
    x = int(input())
    if x == 0:
        print(-heapq.heappop(queue))
    else:
        heapq.heappush(queue, -x)
