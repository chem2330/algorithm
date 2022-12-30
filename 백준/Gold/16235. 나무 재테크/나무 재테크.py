N, M, K = map(int, input().split())  # 땅의 크기(N * N), 나무 개수(M), 년수(K)

arr = [[5] * N for _ in range(N)]
winter = [list(map(int, input().split())) for _ in range(N)]

trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for _ in range(K):
    tmp3 = []
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            tree = trees[i][j]
            if tree:
                tree.sort()
                tmp1 = []
                tmp2 = 0
                for k in tree:
                    if arr[i][j] >= k:
                        arr[i][j] -= k
                        tmp1.append(k + 1)
                        if (k + 1) % 5 == 0:
                            tmp3.append([i, j])
                    else:
                        tmp2 += k // 2
                trees[i][j] = tmp1
                arr[i][j] += tmp2
    # 가을
    for i, j in tmp3:
        for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                trees[ni][nj].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += winter[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])
print(ans)