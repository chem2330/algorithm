# import itertools

# def solution(n, k):
#     pers = list(itertools.permutations(range(1, n+1)))
#     return list(pers[k-1])

import math

def solution(n, k):
    lst = list(range(1, n + 1))
    answer = []
    for _ in range(n - 1):
        tmp = lst.pop((k-1) // math.factorial(len(lst) - 1))
        k = k % math.factorial(len(lst))
        answer.append(tmp)
    answer.append(lst[0])
    return answer