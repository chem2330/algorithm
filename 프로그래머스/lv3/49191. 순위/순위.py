def solution(n, results):
    answer = 0
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i, j in results:
        arr[i][j] = 1  # i가 j에게 이김 -> 1
        arr[j][i] = -1  # j가 i에게 짐 -> -1
    
    # i, j의 직접적 관계는 모르고, i > k > j인 경우 
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j or arr[i][j] == 1 or arr[i][j] == -1:
                    continue
                if arr[i][k] == 1 and arr[k][j] == 1:  # i > k > j인 경우
                    arr[i][j] = 1  # i > j
                    arr[j][i] = arr[k][i] = arr[j][k] = -1  # j < k < i 도 기록
    for row in arr:
        if row.count(0) == 2:  # 0번째 인덱스랑 본인 것만 0이고 나머지는 지거나 이겼을 경우
            answer += 1  # 순위를 알 수 있음
    return answer