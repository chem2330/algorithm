k = int(input())  # 트리의 높이
arr = [0, 0] + list(map(int, input().split()))
# print(arr) = [0, 0, 2, 2, 2, 1, 1, 3]

answer = sum(arr)
for i in range(len(arr) - 1, 1, -2):
    tmp = [arr[i], arr[i - 1]]
    answer += (max(tmp) - min(tmp))
    arr[i // 2] += max(tmp)
print(answer)

