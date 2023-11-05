N = int(input())
health = [0] + list(map(int, input().split()))
pleasure = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        h, p = health[i], pleasure[i]
        if j >= h:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-h] + p)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])