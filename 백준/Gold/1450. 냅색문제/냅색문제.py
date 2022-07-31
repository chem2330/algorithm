import itertools


N, C = map(int, input().split())  # 물건의 수, 최대 무게
arr = list(map(int, input().split()))  # 물건의 무게들

middle = N // 2
arr1 = arr[:middle]
arr2 = arr[middle:]

sum1 = []
sum2 = []

for i in range(len(arr1) + 1):
    combin1 = itertools.combinations(arr1, i)
    for c in combin1:
        sum1.append(sum(c))

for i in range(len(arr2) + 1):
    combin2 = itertools.combinations(arr2, i)
    for c in combin2:
        sum2.append(sum(c))

# print(sum1)
# print(sum2)

ans = 0
sum2.sort()
for i in sum1:
    if i <= C:
        start = 0
        end = len(sum2) - 1
        while start <= end:
            mid = (start + end) // 2

            if sum2[mid] + i > C:
                end = mid - 1
            else:
                start = mid + 1
        ans += end + 1
print(ans)