import sys
import collections


input = sys.stdin.readline

N, M = map(int, input().split())  # 헛간의 개수, 소들의 길
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())  # 헛간위치1, 헛간위치2, 소들의 수
    arr[a].append([c, b])
    arr[b].append([c, a])

now = 1
ans = [500000000] * (N + 1)
ans[1] = 0
q = collections.deque([1])
while q:
    queue = q.popleft()
    for cnt, e in arr[queue]:
        if ans[queue] + cnt < ans[e]:
            ans[e] = ans[queue] + cnt
            q.append(e)
print(ans[N])