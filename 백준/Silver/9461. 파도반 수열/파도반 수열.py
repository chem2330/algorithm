T = int(input())

arr = []

for _ in range(T):
    N = int(input())
    arr.append(N)

memo = [0] * (max(arr) + 1)
memo[1] = memo[2] = memo[3] = 1
for i in range(4, max(arr) + 1):
    memo[i] = memo[i - 3] + memo[i - 2]

for i in arr:
    print(memo[i])