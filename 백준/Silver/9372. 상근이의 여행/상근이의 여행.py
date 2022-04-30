import sys

input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())  # 국가의 수, 비행기 종류
    for _ in range(M):
        s, e = map(int, input().split())
    print(N - 1)