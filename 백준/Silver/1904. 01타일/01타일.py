N = int(input())

arr = [0] * (N + 2)
arr[1] = 1
arr[2] = 2
for i in range(3, N + 1):
    arr[i] = (arr[i - 2] + arr[i - 1]) % 15746

print(arr[N])