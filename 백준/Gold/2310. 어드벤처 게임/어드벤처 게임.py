import sys


input = sys.stdin.readline


def DFS(x, cost):
    global flag
    if flag:
        return
    if x == n:
        flag = 1
        return
    for i in arr[x]:
        if not visited[i]:
            if room_info[i][0] == 0:
                visited[i] = 1
                DFS(i, cost)
                visited[i] = 0
            elif room_info[i][0] == 1:
                visited[i] = 1
                if cost < room_info[i][1]:
                    DFS(i, room_info[i][1])
                else:
                    DFS(i, cost)
                visited[i] = 0
            elif room_info[i][0] == 2 and cost >= room_info[i][1]:
                visited[i] = 1
                DFS(i, cost - room_info[i][1])
                visited[i] = 0


while True:
    n = int(input())  # 미로의 방 수
    if n == 0:
        break
    # E: 빈 방, L: 레프리콘, T: 트롤
    room_info = [[] for _ in range(n + 1)]
    arr = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        tmp = list(input().split())
        if tmp[0] == "E":
            room_info[i] = [0, int(tmp[1])]
        elif tmp[0] == "L":
            room_info[i] = [1, int(tmp[1])]
        elif tmp[0] == "T":
            room_info[i] = [2, int(tmp[1])]
        arr[i] = list(map(int, tmp[2:-1]))
    visited = [0] * (n + 1)
    flag = 0
    DFS(1, 0)
    if flag:
        print("Yes")
    else:
        print("No")