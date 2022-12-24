import sys
import copy


input = sys.stdin.readline

R, C, T = map(int, input().split())  # 집의 크기(R * C),
arr = [list(map(int, input().split())) for _ in range(R)]
air1 = air2 = -1
for i in range(R):
    if arr[i][0] == -1:
        if air1 == -1:
            air1 = i
        else:
            air2 = i
for _ in range(T):
    arr2 = copy.deepcopy(arr)
    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5 and arr[i][j] != -1:
                cnt = 0
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr2[ni][nj] != -1:
                        cnt += 1
                        arr2[ni][nj] += arr[i][j] // 5
                arr2[i][j] -= cnt * (arr[i][j] // 5)
    # 공기청정기
    arr3 = copy.deepcopy(arr2)
    for j in range(2, C):
        arr3[air1][j] = arr2[air1][j - 1]
        arr3[air2][j] = arr2[air2][j - 1]
    arr3[air1][1] = arr3[air2][1] = 0
    for j in range(C - 2, -1, -1):
        arr3[0][j] = arr2[0][j + 1]
        arr3[R - 1][j] = arr2[R - 1][j + 1]
    for i in range(1, air1):
        arr3[i][0] = arr2[i - 1][0]
    for i in range(air2 + 1, R):
        arr3[i][C - 1] = arr2[i - 1][C - 1]
    for i in range(R - 2, air2, -1):
        arr3[i][0] = arr2[i + 1][0]
    for i in range(air1 - 1, -1, -1):
        arr3[i][C - 1] = arr2[i + 1][C - 1]
    arr = arr3
ans = 0
for i in range(R):
    ans += sum(arr[i])
print(ans + 2)