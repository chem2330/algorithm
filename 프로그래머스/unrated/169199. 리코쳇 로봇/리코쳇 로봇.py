def solution(board):
    # answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[10000000] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                arr[i][j] = 0
                si, sj = i, j
    
    queue = [(si, sj, 0)]
    while True:
        if not queue:
            break
            
        x, y, l = queue.pop(0)
        if board[x][y] == "G":
            return l
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for k in range(100):
                nx, ny = x + dx * k, y + dy * k
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == "D":
                    tx, ty = nx - dx, ny - dy
                    if arr[tx][ty] > l + 1:
                        arr[tx][ty] = l + 1
                        queue.append((tx, ty, l + 1))
                    break
                    
    
    return -1