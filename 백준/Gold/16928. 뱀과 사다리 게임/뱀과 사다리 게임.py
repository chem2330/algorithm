N, M = map(int, input().split())  # 사다리, 뱀의 수

jump = {}
for i in range(N + M):
    a, b = map(int, input().split())
    jump[a] = b

arr = [1000] * 101
arr[1] = 0

deque = [1]

while deque:
    q = deque.pop(0)
    for i in range(6, 0, -1):
        if q + i <= 100:
            if jump.get(q + i):
                if arr[jump.get(q + i)] > arr[q] + 1:
                    arr[jump.get(q + i)] = arr[q] + 1
                    deque.append(jump.get(q + i))
            else:
                if arr[q + i] > arr[q] + 1:
                    arr[q + i] = arr[q] + 1
                    deque.append(q + i)
print(arr[100])