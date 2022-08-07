n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)

if n <= 2:
    print(sum(arr))
else:
    tmp = arr[:]  # 얕은 복사(tmp = 원본)
    arr[1] = arr[0] + arr[1]
    arr[2] = max(tmp[1] + tmp[2], tmp[0] + tmp[2])

    for i in range(3, n):
        arr[i] = max(max(arr[:i - 2]) + tmp[i - 1] + tmp[i], max(arr[:i - 1]) + tmp[i])
    print(max(arr))