N = int(input())  # 공간의 크기
arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(N):
        if tmp[j] == 9:
           now = [i, j]

arr[now[0]][now[1]] = 0
shark_size = 2
shark_eat = 0
answer = 0

def check_fish(s_x, s_y):
    visited = [[0] * N for _ in range(N)]
    queue1 = [[[s_x, s_y]]]
    shark_list = []
    time = 0
    while queue1 != [[]]:
        queue2 = queue1.pop(0)
        time += 1
        for x, y in queue2:
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] <= shark_size:
                    visited[nx][ny] = 1
                    queue1.append([nx, ny])
                    if 0 < arr[nx][ny] < shark_size:
                        shark_list.append([nx, ny])
        if shark_list:
            return sorted(shark_list)[0], time
        queue1 = [queue1]
    return 0, 0

while True:
    shark, time = check_fish(now[0], now[1])
    if shark:
        answer += time
        arr[shark[0]][shark[1]] = 0
        now = shark
        shark_eat += 1
        if shark_eat == shark_size:
            shark_size += 1
            shark_eat = 0
    else:
        break
print(answer)