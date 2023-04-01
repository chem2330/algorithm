import sys


input = sys.stdin.readline

M = int(input())
S = [0] * 21

for _ in range(M):
    tmp = input().split()
    if tmp[0] == 'add':
        S[int(tmp[1])] = 1
    elif tmp[0] == 'remove':
        S[int(tmp[1])] = 0
    elif tmp[0] == 'check':
        print(S[int(tmp[1])])
    elif tmp[0] == 'toggle':
        S[int(tmp[1])] = (S[int(tmp[1])] + 1) % 2
    elif tmp[0] == 'all':
        S = [1] * 21
    elif tmp[0] == 'empty':
        S = [0] * 21
