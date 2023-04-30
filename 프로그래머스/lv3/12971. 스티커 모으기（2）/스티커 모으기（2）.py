def solution(sticker):
    l = len(sticker)
    def dfs(i, ssum):
        nonlocal answer
        if i >= l:
            if ssum > answer:
                answer = ssum
            return
        if i == l - 1:
            if not visited[0]:
                visited[i] = 1
                dfs(i + 2, ssum + sticker[i])
                visited[i] = 0
        else:
            visited[i] = 1
            dfs(i + 2, ssum + sticker[i])
            visited[i] = 0
        if i + 1 < l:
            visited[i + 1] = 1
            dfs(i + 3, ssum + sticker[i + 1])
            visited[i + 1] = 0
        return
    answer = 0
    visited = [0] * l
    dfs(0, 0)
    return answer