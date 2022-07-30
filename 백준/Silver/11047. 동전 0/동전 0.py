N, K = map(int, input().split())  # 동전 개수, 만들 금액
arr = []
for _ in range(N):
    x = int(input())
    arr.insert(0, x)

ans = 0
for coin in arr:
    ans += K // coin
    K = K % coin
print(ans)