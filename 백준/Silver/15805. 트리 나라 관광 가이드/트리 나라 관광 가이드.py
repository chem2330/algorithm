N = int(input())
arr = list(map(int, input().split()))
K = max(arr) + 1  # 총 노드 수
print(K)
P = [-2] * K
P[arr[0]] = -1
visited = [0] * K
visited[arr[0]] = 1

for i in range(1, N):
    if not visited[arr[i]]:
        visited[arr[i]] = 1
        P[arr[i]] = arr[i - 1]
print(*P)