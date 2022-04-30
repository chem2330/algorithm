N = int(input())
step = [0, 0]
for _ in range(N):
    step.append(int(input()))

memo = [[0, 0], [0, 0]] + [[0] * 2 for _ in range(N)]
for i in range(2, N + 2):
    memo[i][0] = max(memo[i - 2]) + step[i]
    memo[i][1] = memo[i-1][0] + step[i]

print(max(memo[-1]))