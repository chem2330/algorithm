import sys


input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
arr.sort(key=lambda x: (x[1], x[0]))

idx = 0
end = 0
ans = 0
while idx < N:
    if arr[idx][0] >= end:
        ans += 1
        end = arr[idx][1]
    idx += 1
print(ans)