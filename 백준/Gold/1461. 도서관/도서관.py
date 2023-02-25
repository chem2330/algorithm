N, M = map(int, input().split())  # 책의 개수, 한번에 들 수 있는 책의 수
arr = sorted(map(int, input().split()))  # 책의 위치
ans = []
for i in range(0, N, M):
    if arr[i] >= 0:
        break
    ans.append(-arr[i])

for i in range(N - 1, -1, -M):
    if arr[i] <= 0:
        break
    ans.append(arr[i])

ans.sort()
print(sum(ans) * 2 - ans[-1])