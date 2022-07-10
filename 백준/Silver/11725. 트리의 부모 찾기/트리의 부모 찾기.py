N = int(input())  # 노드의 수
arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

P = [0] * (N + 1)

stack = [1]
while stack:
    v = stack.pop()
    for i in arr[v]:
        if P[i] == 0:
            P[i] = v
            stack.append(i)
for i in P[2:]:
    print(i)