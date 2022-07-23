import sys
import heapq


input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if queue:
            print(heapq.heappop(queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(queue, [abs(x), x])