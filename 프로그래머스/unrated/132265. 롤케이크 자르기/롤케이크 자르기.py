from collections import Counter

def solution(topping):
    answer = 0
    # l = len(set(topping))
    # if l % 2:
    #     return 0
    tmp1 = {}
    tmp2 = Counter(topping)
    for t in topping:
        if tmp1.get(t):
            tmp1[t] += 1
        else:
            tmp1[t] = 1
        tmp2[t] -= 1
        if tmp2[t] == 0:
            del tmp2[t]
        if len(tmp1) == len(tmp2):
            answer += 1
        elif len(tmp1) > len(tmp2):
            break
    return answer