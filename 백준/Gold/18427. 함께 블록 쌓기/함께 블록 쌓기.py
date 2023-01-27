import sys
from collections import Counter


input = sys.stdin.readline


N, M, H = map(int, input().split())  # 학생 수, 최대 블록 수, 목표 높이
info = []
for _ in range(N):
    info.append(list(map(int, input().split())) + [0])

dp = Counter(info[0])
for k in range(1, N):
    tmp = {}
    for i in info[k]:
        for j in dp.keys():
            if i + j <= H:
                if i + j not in tmp:
                    tmp[i + j] = dp[j]
                else:
                    tmp[i + j] += dp[j]
    dp = tmp

print(dp[H] % 10007)