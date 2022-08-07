n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    memo = [0] * (n + 1)
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 2] + memo[i - 1]
    print(memo[-1])
