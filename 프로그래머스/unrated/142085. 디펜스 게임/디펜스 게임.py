from heapq import heappop, heappush


def solution(n, k, enemy):
    answer = 0
    lst = []
    
    for e in enemy:
        heappush(lst, -e)
        n -= e
        if n < 0:
            if k == 0:
                break
            n -= heappop(lst) 
            k -= 1
        answer += 1
    return answer



# def solution(n, k, enemy):
#     num = len(enemy)
#     if k >= num:
#         return num
    
#     i = k
#     lst1 = enemy[:k]  # 무적권
#     while True:
#         if min(lst1) < enemy[i]:
#             lst1.append(enemy[i])
#             n -= min(lst1)
#             lst1.remove(min(lst1))
#         else:
#             n -= enemy[i]
#         if n <= 0 or i == num - 1:
#             return i
#         i += 1