def bfs(start, total):
    global max_short
    for i in range(N):
        if arr[i][0] >= start and arr[i][1] <= D:
            bfs(arr[i][1], total + arr[i][2])
    else:
        if total > max_short:
            max_short = total
        return


N, D = map(int, input().split())  # 지름길 개수, 고속도로 길이
arr = []
for _ in range(N):
    S, E, L = map(int, input().split())
    arr.append([S, E, (E - S) - L])

max_short = 0
bfs(0, 0)

print(D - max_short)