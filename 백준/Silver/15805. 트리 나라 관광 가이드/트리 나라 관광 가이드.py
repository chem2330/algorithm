N = int(input())
arr = list(map(int, input().split()))
K = max(arr) + 1  # 총 노드 수
print(K)

P = [-1] * K  # 각 노드의 부모 리스트 (루트 빼고 다 갱신 -1 넣어둠)
visited = [0] * K
visited[arr[0]] = 1

for i in range(1, N):
    if not visited[arr[i]]:
        visited[arr[i]] = 1
        P[arr[i]] = arr[i - 1]
print(*P)