import itertools


N = int(input())
arr = []  # 학생 S, 선생님 T, 그 외 X
arr_T = []
arr_X = []
for i in range(N):
    tmp = input().split()
    arr.append(tmp)
    for j in range(N):
        if tmp[j] == 'T':
            arr_T.append([i, j])
        elif tmp[j] == 'X':
            arr_X.append([i, j])

combinations = list(itertools.combinations(arr_X, 3))
flag1 = 0
for combination in combinations:
    flag2 = 0
    for i, j in combination:
        arr[i][j] = 'O'
    for x, y in arr_T:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            for k in range(1, N):
                nx, ny = x + k * dx, y + k * dy
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == 'S':
                        flag2 = 1
                        break
                    elif arr[nx][ny] == 'T' or arr[nx][ny] == 'O':
                        break
                else:
                    break
    if not flag2:
        print('YES')
        flag1 = 1
        break

    for i, j in combination:
        arr[i][j] = 'X'

if not flag1:
    print('NO')