# from collections import deque


def solution(x, y, n):
    lst = [10000000] * (y + 1)
    queue = set([x])
    lst[x] = 0
    while queue:
        q = queue.pop()
        if q * 3 <= y and lst[q * 3] > lst[q] + 1:
            queue.add(q * 3)
            lst[q * 3] = lst[q] + 1
        if q * 2 <= y and lst[q * 2] > lst[q] + 1:
            queue.add(q * 2)
            lst[q * 2] = lst[q] + 1
        if q + n <= y and lst[q + n] > lst[q] + 1:
            queue.add(q + n)
            lst[q + n] = lst[q] + 1

    if lst[y] == 10000000:
        return -1
    return lst[y]