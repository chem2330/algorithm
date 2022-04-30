import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())  # 국가의 수, 비행기 종류
    # arr = [[] for _ in range(N)]
    for _ in range(M):
        s, e = map(int, input().split())
        # arr[s - 1].append(e - 1)
        # arr[e - 1].append(s - 1)
    print(N - 1)