N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]

min_price = price[0]
ans = min_price * distance[0]
for i in range(1, N - 1):
    if price[i] < min_price:
        min_price = price[i]
    ans += min_price * distance[i]

print(ans)