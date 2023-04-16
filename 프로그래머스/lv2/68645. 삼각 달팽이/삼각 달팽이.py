def solution(n):
    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0
    flag = 0
    for i in range(1, n * (n + 1) // 2 + 1):
        arr[x][y] = i
        if flag == 0:
            if x < n - 1 and not arr[x + 1][y]:
                x += 1
            else:
                flag = 1
                y += 1
        elif flag == 1:
            if y < n - 1 and not arr[x][y + 1]:
                y += 1
            else:
                flag = 2
                x -= 1
                y -= 1
        elif flag == 2:
            if not arr[x - 1][y - 1]:
                x -= 1
                y -= 1
            else:
                flag = 0
                x += 1
    answer = []
    for i in range(n):
        for j in range(i + 1):
            answer.append(arr[i][j])
    return answer