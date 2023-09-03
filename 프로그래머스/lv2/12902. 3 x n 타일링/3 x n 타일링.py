def solution(n):
    lst = [0 for _ in range(n + 1)]
    lst[0], lst[2], lst[4] = 1, 3, 11
    for i in range(6, n + 1, 2):
        lst[i] = lst[i - 2] * 3
        for j in range(i - 4, -1, -2):
            lst[i] += lst[j] * 2
        lst[i] = lst[i] % 1000000007
    return lst[n]