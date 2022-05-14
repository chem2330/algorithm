import sys

input = sys.stdin.readline


def find_set(x):
    while x != v[x]:
        x = v[x]
    return x


V, E = map(int, input().split())
edge = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    edge.append((w, v1, v2))
edge.sort()  # 가중치 작은 것부터 오름차순정렬

cnt = 0
total = 0
v = list(range(V + 1))  # 정점들
for w, v1, v2 in edge:
    v1_root = find_set(v1)
    v2_root = find_set(v2)
    if v1_root != v2_root:
        if v1_root > v2_root:
            v[v1_root] = v2_root
        else:
            v[v2_root] = v1_root
        cnt += 1
        total += w
        if cnt == V - 1:
            break
print(total)