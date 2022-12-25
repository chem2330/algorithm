import sys
import copy


N, M = map(int, input().split())  # 행렬 크기(N * M)
arr = []
CCTV = []
all = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(M):
        if 0 < tmp[j] < 6:
            CCTV.append([tmp[j], i, j])
        if not tmp[j]:
            all += 1

dir = [[],
       [[(1, 0)], [(0, 1)], [(-1, 0)], [(0, -1)]],
       [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
       [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
       [[(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)], [(0, -1), (-1, 0), (0, 1)]],
       [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
       ]

dir_len = [0, 4, 2, 4, 4, 1]
max_cnt = 0
def pick(i, cnt, area):
    global max_cnt
    if i == len(CCTV):
        if cnt > max_cnt:
            max_cnt = cnt
        return
    for k in range(dir_len[CCTV[i][0]]):
        area2 = copy.deepcopy(area)
        cnt2 = cnt
        for dx, dy in dir[CCTV[i][0]][k]:
            for p in range(1, 9):
                nx, ny = CCTV[i][1] + p * dx, CCTV[i][2] + p * dy
                if 0 <= nx < N and 0 <= ny < M and area[nx][ny] != 6:
                    if area[nx][ny] == 0 and area[nx][ny] != -1:
                        area2[nx][ny] = -1
                        cnt2 += 1
                else:
                    break
        pick(i + 1, cnt2, area2)

pick(0, 0, arr)
print(all - max_cnt)