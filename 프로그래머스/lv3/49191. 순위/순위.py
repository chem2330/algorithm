def solution(n, results):
    answer = 0
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i, j in results:
        arr[i][j] = 1
        arr[j][i] = -1
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j or arr[i][j] in [1, -1]:
                    continue
                if arr[i][k] == arr[k][j] == 1:
                    arr[i][j] = 1
                    arr[j][i] = arr[k][i] = arr[j][k] = -1
    for row in arr:
        if row.count(0) == 2:
            answer += 1
    return answer