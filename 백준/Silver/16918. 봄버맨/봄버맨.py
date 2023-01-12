R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
elif N == 1:
    for i in range(R):
        print(''.join(arr[i]))
else:
    ans = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':
                for di, dj in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        ans[ni][nj] = '.'
    if N % 4 == 3:
        for i in range(R):
            print(''.join(ans[i]))
    elif N % 4 == 1:
        ans2 = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if ans[i][j] == 'O':
                    for di, dj in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < R and 0 <= nj < C:
                            ans2[ni][nj] = '.'
        for i in range(R):
            print(''.join(ans2[i]))