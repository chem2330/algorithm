n = int(input())

result = [0] * (n + 1)
first = int(input())
result[1] = first
for i in range(2, n + 1):  # i 번째 줄
    line = list(map(int, input().split()))
    tmp = result[:]
    for j in range(1, i + 1):
        if j == 1:
            result[j] = tmp[j] + line[j - 1]
        elif j == i:
            result[j] = tmp[j - 1] + line[j - 1]
        else:
            result[j] = max(tmp[j], tmp[j - 1]) + line[j - 1]
print(max(result))