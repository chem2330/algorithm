import collections


N = int(input())
inf = N
arr = [inf] * (N + 1)

tmp = 1
queue = collections.deque([1])
arr[1] = 0
while queue:
    q = queue.popleft()
    if q + 1 <= N and arr[q + 1] > arr[q] + 1:
        arr[q + 1] = arr[q] + 1
        queue.append(q + 1)
    if q * 2 <= N and arr[q * 2] > arr[q] + 1:
        arr[q * 2] = arr[q] + 1
        queue.append(q * 2)
    if q * 3 <= N and arr[q * 3] > arr[q] + 1:
        arr[q * 3] = arr[q] + 1
        queue.append(q * 3)
print(arr[N])