def solution(dirs):
    answer = 0
    visited = [[[0] * 2 for _ in range(11)] for _ in range(11)]
    x = y = 5
    for s in dirs:
        if s == "L":
            if y == 0:
                continue
            if visited[x][y-1][0] == 0:
                visited[x][y-1][0] = 1
                answer += 1
            y -= 1
        elif s == "R":
            if y == 10:
                continue
            if visited[x][y][0] == 0:
                visited[x][y][0] = 1
                answer += 1
            y += 1
        elif s == "U":
            if x == 0:
                continue
            if visited[x-1][y][1] == 0:
                visited[x-1][y][1] = 1
                answer += 1
            x -= 1
        elif s == "D":
            if x == 10:
                continue
            if visited[x][y][1] == 0:
                visited[x][y][1] = 1
                answer += 1
            x += 1
    return answer