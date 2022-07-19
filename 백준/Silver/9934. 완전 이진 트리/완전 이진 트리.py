def preorder(root):
    global idx
    if root < 2 ** K:
        preorder(root * 2)
        idx += 1
        arr[root] = pre_order[idx]
        preorder(root * 2 + 1)


K = int(input())
pre_order = list(map(int, input().split()))  # 후위순회
arr = [0] * (2 ** K)
idx = -1
preorder(1)
# print(arr)  # [0, 3, 6, 2, 1, 4, 5, 7]
arr = arr[1:]
for i in range(K):
    print(*arr[:2 ** i])
    arr = arr[2 ** i:]