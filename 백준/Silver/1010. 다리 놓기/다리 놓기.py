T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = 1
    for i in range(N):
        ans = ans * (M - i) / (i + 1)
    print(int(ans))