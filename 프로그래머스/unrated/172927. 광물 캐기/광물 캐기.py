def solution(picks, minerals):
    answer = 0
    n = min(sum(picks) * 5, len(minerals))
    m = 0
    lst = []
    tmp = [0, 0, 0]
    
    for i in range(n):
        m += 1
        if minerals[i] == "diamond":
            tmp[0] += 1
        elif minerals[i] == "iron":
            tmp[1] += 1
        else:
            tmp[2] += 1
        if m == 5 or i == n -1:
            lst.append(tmp)
            m = 0
            tmp = [0, 0, 0]
    lst = sorted(lst, reverse = True)
    while True:
        if lst:
            tmp = lst.pop(0)
        else:
            break
        if picks[0]:
            answer += tmp[0] + tmp[1] + tmp[2]
            picks[0] -= 1
        elif picks[1]:
            answer += tmp[0] * 5 + tmp[1] + tmp[2]
            picks[1] -= 1
        elif picks[2]:
            answer += tmp[0] * 25 + tmp[1] * 5 + tmp[2]
            picks[2] -= 1
    return answer