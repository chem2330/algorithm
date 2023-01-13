N = int(input())
arr = [-1] * 11
ans = 0
for _ in range(N):
    n, d = map(int, input().split())  # 번호, 방향
    if arr[n] != -1 and arr[n] != d:
        ans += 1
    arr[n] = d
print(ans)