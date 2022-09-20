def solution(begin, target, words):
    if target not in words:  # 이 경우는 변환할 수 없으니 0 리턴
        return 0
    visited = [100] * len(words)  # 몇 단계에 걸쳐 변환될 수 있는지 적는 리스트 / 초기는 inf 값으로 넣어둠
    word_len = len(begin)  # 각 단어의 길이
    words_len = len(words)  # words 리스트 길이

    stack = [[begin, 0]]  # [단어, 변환 횟수]
    while stack:
        v = stack.pop()
        for i in range(words_len):  # 모든 words에 대해
            tmp = 0  # 겹치지 않는 알파벳 수
            for j in range(word_len):  # 알파벳 하나씩 조회하면서
                if v[0][j] != words[i][j]:  # 같지 않으면
                    tmp += 1  # 추가
                    if tmp >= 2:  # 2개 이상 다르면 바로 break
                        break
            if tmp == 1:  # 알파벳이 1개만 다르고
                if visited[i] > v[1] + 1:  # 변환 횟수를 갱신할 수 있으면
                    visited[i] = v[1] + 1  # 갱신하고
                    stack.append([words[i], v[1] + 1])  # 변환 횟수 1 늘리고, stack에 추가
    found_idx = words.index(target)  # target의 idx 찾기
    if visited[found_idx] == 100:  # 변환 횟수가 그대로 inf면 변환할 수 없는 경우
        return 0
    return visited[found_idx]  # 그 외에는 변환 횟수 출력