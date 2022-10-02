def solution(m, n, puddles):
    arr = [[-1 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        arr[puddle[1] - 1][puddle[0] - 1] = 0
    arr[0][0] = 1
    
    flag = 0
    for j in range(1, m):
        if arr[0][j] == 0:
            flag = 1
        if flag == 0:
            arr[0][j] = 1
        else:
            arr[0][j] = 0
    for i in range(1, n):
        for j in range(m):
            if arr[i][j] == -1:
                if j == 0:
                    if arr[i - 1][j] > 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0
                else:
                    arr[i][j] = (arr[i - 1][j] + arr[i][j - 1]) % 1000000007
                
    return arr[-1][-1]