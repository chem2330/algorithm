N, K = map(int, input().split())  # 준서가 가져갈 개수, 버틸 수 있는 무게
things = []
for _ in range(N):
    W, V = map(int, input().split())
    things.append([W, V])

arr = [[0] * (K + 1) for _ in range(N)]
for j in range(things[0][0], K + 1):
    arr[0][j] = things[0][1]
# print(arr)

for i in range(1, N):
    thing_weight, thing_value = things[i]
    for j in range(1, K + 1):
        if j < thing_weight:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - thing_weight] + thing_value)
print(arr[-1][-1])