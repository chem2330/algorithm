def solution(order):
    answer = 0
    belt = []
    idx = 0
    for i in range(1, len(order) + 1):
        if order[idx] == i:
            answer += 1
            idx += 1
            while True:
                if belt and belt[-1] == order[idx]:
                    belt.pop()
                    answer += 1
                    idx += 1
                else:
                    break
        else:
            belt.append(i)
    return answer