import sys


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr) = [-99, -2, -1, 4, 98]

solution = 10000000000
start = 0
end = N - 1

while start < end:
    if abs(arr[start] + arr[end]) < solution:
        solution = abs(arr[start] + arr[end])
        ans = [arr[start], arr[end]]
    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1

print(*ans)
