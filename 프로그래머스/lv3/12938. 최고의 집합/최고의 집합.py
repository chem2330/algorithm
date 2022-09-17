def solution(n, s):
    if n > s:
        answer = [-1]
    else:
        answer = [int(s // n)] * n
        tmp = s - sum(answer)
        for i in range(tmp):
            answer[n - 1 - i] += 1
    
    return answer