N = int(input())  # 공간의 크기
arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(N):
        if tmp[j] == 9:  # 상어 위치 now에 저장
           now = [i, j]

arr[now[0]][now[1]] = 0  # 상어 위치 지나갈 수 있으므로 0으로 바꿔둠
shark_size = 2  # 현재 상어 크기
shark_eat = 0  # 상어가 먹은 물고기 수
answer = 0  # 정답 변수

def check_fish(s_x, s_y):  # 현재 위치에서 먹을 수 있는 물고기 확인하는 함수
    visited = [[0] * N for _ in range(N)]
    queue1 = [[[s_x, s_y]]]
    shark_list = []  # 먹을 수 있는 물고기의 위치 리스트
    time = 0  # 이동한 거리 = 시간
    while queue1 != [[]]:
        queue2 = queue1.pop(0)
        time += 1
        for x, y in queue2:
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] <= shark_size:  # 상어 크기보다 작거나 같으면 이동 가능
                    visited[nx][ny] = 1
                    queue1.append([nx, ny])
                    if 0 < arr[nx][ny] < shark_size:  # 상어 크기보다 작으면 먹을 수 있음
                        shark_list.append([nx, ny])
        if shark_list:
            return sorted(shark_list)[0], time  # 왼쪽 위에 있는 물고기 하나랑 시간 return
        queue1 = [queue1]
    return 0, 0   # 종료될 때 return 값(나중에 에러 안 나기 위해)

while True:
    fish, time = check_fish(now[0], now[1])
    if fish:  # 먹을 수 있는 물고기가 있으면
        now = fish  # 그 위치로 이동
        answer += time
        arr[fish[0]][fish[1]] = 0
        shark_eat += 1  # 먹은 개수 추가
        if shark_eat == shark_size:  # 사이즈 업
            shark_size += 1
            shark_eat = 0
    else:  # 종료 조건
        break
print(answer)