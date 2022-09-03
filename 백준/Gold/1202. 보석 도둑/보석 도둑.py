import sys
import heapq


input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    M, V = map(int, input().split())  # 무게, 비용
    heapq.heappush(gems, [M, V])

bags = []
for _ in range(K):
    C = int(input())
    bags.append(C)
bags.sort()

ans = 0
stack = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        weight, price = heapq.heappop(gems)
        heapq.heappush(stack, -price)
    if stack:
        ans += -heapq.heappop(stack)
print(ans)