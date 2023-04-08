def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        tmp = number[:]
        for d in discount[i:i + 10]:
            for j in range(len(want)):
                if d == want[j] and tmp[j] > 0:
                    tmp[j] -= 1
        if sum(tmp) == 0:
            answer += 1
    return answer