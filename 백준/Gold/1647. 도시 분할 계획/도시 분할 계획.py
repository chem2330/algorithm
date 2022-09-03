import sys


input = sys.stdin.readline


def find_set(x):
    while x != p[x]:  # 대표원소가 아니면
        x = p[x]  # x가 가리키는 정점으로 이동
    return x

def union(a, b):
    a = find_set(a)
    b = find_set(b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append([C, A, B])

edges.sort()
p = [i for i in range(N + 1)]  # 대표원소 초기화

node = [0] * (N + 1)
ans = 0
cnt = 0
for cost, a, b in edges:
    if find_set(a) != find_set(b):
        cnt += 1
        ans += cost
        union(a, b)
        if cnt == N - 2:
            break
print(ans)