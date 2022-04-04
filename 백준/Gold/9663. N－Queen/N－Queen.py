def dfs(i):
    global cnt
    if i == N:
        cnt += 1
        return

    for j in range(N):
        if check1[j] == 0 and check2[i + j] == 0 and check3[i - j + (N - 1)] == 0:
            check1[j] = 1
            check2[i + j] = 1
            check3[i - j + (N - 1)] = 1
            dfs(i + 1)
            check1[j] = 0
            check2[i + j] = 0
            check3[i - j + (N - 1)] = 0
    return



N = int(input())  # N * N 행렬에 N개 퀸 놓기
check1 = [0] * N
check2 = [0] * (2 * N + 1)
check3 = [0] * (2 * N + 1)
cnt = 0
dfs(0)
print(cnt)