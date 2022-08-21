def Quad_Tree(x, y, n):
    ssum = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            ssum += arr[i][j]

    if ssum == 0:
        return 0
    elif ssum == n ** 2:
        return 1
    else:
        new_n = n // 2
        return "(" + str(Quad_Tree(x, y, new_n)) + str(Quad_Tree(x, y + new_n, new_n)) + str(Quad_Tree(x + new_n, y, new_n)) + str(Quad_Tree(x + new_n, y + new_n, new_n)) + ")"

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
print(Quad_Tree(0, 0, N))