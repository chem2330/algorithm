def solution(cards):
    answer = 0
    visited = [0] * len(cards)
    idx = 0
    answer_lst = []
    while idx < len(cards):
        if visited[idx]:
            idx += 1
            continue
        cnt = 1
        visited[idx] = 1
        tmp = cards[idx] - 1
        while True:
            if visited[tmp]:
                answer_lst.append(cnt)
                break
            cnt += 1
            visited[tmp] = 1
            tmp = cards[tmp] - 1
    answer_lst.append(0)
    answer_lst.sort()
    return answer_lst[-1] * answer_lst[-2]