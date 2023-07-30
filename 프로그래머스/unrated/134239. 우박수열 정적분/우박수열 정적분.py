def solution(k, ranges):
    answer = []
    lst = [k]
    
    while True:
        tmp = lst[-1]
        if tmp == 1:
            break
        if tmp % 2:
            lst.append(tmp * 3 + 1)
        else:
            lst.append(tmp // 2)
    
    area_lst = []
    for i in range(len(lst) - 1):
        area_lst.append(lst[i] + lst[i + 1])
    
    
    n = len(lst) - 1
    for i, j in ranges:
        if i == n + j:
            answer.append(0)
        elif i > n + j:
            answer.append(-1)
        else:
            tmp = 0
            s, e = i, n + j
            for ii in range(s, e):
                tmp += area_lst[ii]
            answer.append(tmp /2)
    
    
    return answer