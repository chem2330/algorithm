from collections import Counter

def solution(weights):
    answer = 0
    # n = len(weights)
    weights = Counter(weights)
    ratio = [1, 1.5, 2, 4/3]
    lst = sorted(weights.keys())
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            tmp = lst[j] / lst[i]
            if tmp in ratio:
                answer += weights[lst[i]] * weights[lst[j]]
    lst2 = weights.values()
    for num in lst2:
        if num > 1:
            answer += num * (num - 1) // 2
                
    return answer