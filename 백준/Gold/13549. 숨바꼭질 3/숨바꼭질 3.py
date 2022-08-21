import heapq




N, K = map(int, input().split())  # 수빈이 위치, 동생 위치
arr = [1000000] * 100001
arr[N] = 0

q = [(0, N)]
while q:
    time, index = heapq.heappop(q)
    if index == K:
        break

    if index * 2 < 100001 and time < arr[index * 2]:
        arr[index * 2] = time
        heapq.heappush(q, (time, index * 2))

    if 0 <= index - 1 and time + 1 < arr[index - 1]:
        arr[index - 1] = time + 1
        heapq.heappush(q, (time + 1, index - 1))
    if index + 1 < 100001 and time + 1 < arr[index + 1]:
        arr[index + 1] = time + 1
        heapq.heappush(q, (time + 1, index + 1))

print(arr[K])