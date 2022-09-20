def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [100] * len(words)
    word_len = len(begin)
    words_len = len(words)

    stack = [[begin, 0]]
    while stack:
        v = stack.pop()
        for i in range(words_len):
            tmp = 0
            for j in range(word_len):
                if v[0][j] != words[i][j]:
                    tmp += 1
                    if tmp >= 2:
                        break
            if tmp == 1:
                if visited[i] > v[1] + 1:
                    visited[i] = v[1] + 1
                    stack.append([words[i], v[1] + 1])
    found_idx = words.index(target)
    if visited[found_idx] == 100:
        return 0
    return visited[found_idx]