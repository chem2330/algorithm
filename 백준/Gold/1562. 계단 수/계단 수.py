N = int(input())

dp = [[0] * 1024 for _ in range(10)]

for i in range(1, 10):
    dp[i][1 << i] = 1

for _ in range(2, N + 1):
    next_dp = [[0] * 1024 for _ in range(10)]

    for i in range(10):
        for j in range(1024):
            if i > 0:
                next_dp[i][j | (1 << i)] += dp[i - 1][j]
                next_dp[i][j | (1 << i)] %= 1000000000
            if i < 9:
                next_dp[i][j | (1 << i)] += dp[i + 1][j]
                next_dp[i][j | (1 << i)] %= 1000000000
    dp = next_dp

ans = 0
for i in range(10):
    ans += dp[i][1023]
    ans %= 1000000000
print(ans)