import sys


input = sys.stdin.readline
sys.setrecursionlimit(500000)

N = int(input())
P = [0] * (N + 1)
C1 = [0] * (N + 1)
C2 = [0] * (N + 1)
for _ in range(N):
    a, b, c = map(int, input().split())  # 현재 노드, 왼쪽 자식 노드, 오른쪽 자식 노드
    if b != -1:
        P[b] = a
        C1[a] = b
    if c != -1:
        P[c] = a
        C2[a] = c


def order(node):
    if node:
        order(C1[node])
        tmp.append(node)
        order(C2[node])


def inorder(node):
    answer.append(node)
    visited[node] = 1
    if C1[node] and visited[C1[node]] == 0:
        inorder(C1[node])
    elif C2[node] and visited[C2[node]] == 0:
        inorder(C2[node])
    elif node == tmp[-1]:
        return
    elif P[node]:
        inorder(P[node])


tmp = []
order(1)
visited = [0] * (N + 1)
answer = []
inorder(1)
print(len(answer) - 1)