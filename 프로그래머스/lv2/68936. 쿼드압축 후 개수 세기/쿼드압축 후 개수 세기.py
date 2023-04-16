def solution(arr):
    N = len(arr)
    cnt_0, cnt_1 = N * N, 0
    for i in range(N):
        cnt_1 += sum(arr[i])
        cnt_0 -= sum(arr[i])

    sizes = [[1] * N for _ in range(N)]
    size = 1
    while True:
        for x in range(0, N, size * 2):
            for y in range(0, N, size * 2):
                if sizes[x][y] == sizes[x][y + size] == sizes[x + size][y] == sizes[x + size][y + size] == size and arr[x][y] == arr[x][y + size] == arr[x + size][y] == arr[x + size][y + size]:
                    sizes[x][y] = size * 2
                    if arr[x][y] == 0:
                        cnt_0 -= 3
                    else:
                        cnt_1 -= 3

        size *= 2
        if size == N:
            break
                    
    
    
    return [cnt_0, cnt_1]