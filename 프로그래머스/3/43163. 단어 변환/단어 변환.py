def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    l_w = len(words)
    l_b = len(begin)
    visited = [0] * l_w

    queue = [[begin, 0]]
    while queue:
        q, l = queue.pop(0)
        if q == target:
            return l
        
        for i in range(l_w):
            cnt = 0
            for j in range(l_b):
                if q[j] != words[i][j]:
                    cnt += 1
                    if cnt > 1:
                        break
            if cnt == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append([words[i], l + 1])
    
    return answer