import sys


input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

i, j = -1, 0
ssum = arr[0]
while True:
    if ssum == M:
        ans += 1
        if j < N - 1:
            j += 1
            i += 1
            ssum += (arr[j] - arr[i])
        else:
            break
    elif ssum < M:
        if j < N - 1:
            j += 1
            ssum += arr[j]
        else:
            break
    elif ssum > M:
        i += 1
        ssum -= arr[i]

print(ans)

