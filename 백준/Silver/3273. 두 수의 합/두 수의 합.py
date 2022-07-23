n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))
arr.sort()
# print(arr) = [1, 2, 3, 5, 7, 9, 10, 11, 12]
x = int(input())

start, end = 0, n - 1
cnt = 0
while start < end:
    if arr[start] + arr[end] == x:
        cnt += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] > x:
        end -= 1
    else:
        start += 1

print(cnt)