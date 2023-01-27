import sys


sys.setrecursionlimit(10**6)


def Change(x):
    if x > 0:
        arr[x - 1] = (arr[x - 1] + 1) % 2
    arr[x] = (arr[x] + 1) % 2
    if x < N - 1:
        arr[x + 1] = (arr[x + 1] + 1) % 2

def DFS(x, n):
    global ans
    if x >= 2 and goal[x - 2] != arr[x - 2]:
        return
    if x == N:
        if arr == goal:
            ans = n
        return
    Change(x)
    DFS(x + 1, n + 1)
    Change(x)

    DFS(x + 1, n)




N = int(input())  # 스위치 개수
arr = list(map(int, list(input())))
goal = list(map(int, list(input())))

ans = -1
DFS(0, 0)
print(ans)