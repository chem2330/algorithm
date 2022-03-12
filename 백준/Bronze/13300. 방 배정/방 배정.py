N, K = map(int, input().split())
two_six = [[0] * 6 for _ in range(2)]
cnt = 0
for _ in range(N):
    gender, grade = map(int, input().split())
    i, j = gender, grade - 1
    two_six[i][j] += 1
    if two_six[i][j] == 1:
        cnt += 1
    if two_six[i][j] > K:
        cnt += 1
        two_six[i][j] = 1

print(cnt)