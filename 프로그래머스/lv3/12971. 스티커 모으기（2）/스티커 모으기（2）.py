def solution(sticker):
    l = len(sticker)
    if l == 1:
        return sticker[0]
    
    arr = [[0 for _ in range(l)] for _ in range(2)]
    arr[0][0] = sticker[0]
    arr[0][1] = sticker[0]
    arr[1][1] = sticker[1]
    
    for i in range(2, l-1):
        arr[0][i] = max(arr[0][i-2]+sticker[i], arr[0][i-1])
    for i in range(2, l):
        arr[1][i] = max(arr[1][i-2]+sticker[i], arr[1][i-1])
    return max(arr[0][l-2], arr[1][l-1])



# def solution(sticker):
#     l = len(sticker)
#     def dfs(i, ssum):
#         nonlocal answer
#         if i >= l:
#             if ssum > answer:
#                 answer = ssum
#             return
#         if i == l - 1:
#             if not visited[0]:
#                 visited[i] = 1
#                 dfs(i + 2, ssum + sticker[i])
#                 visited[i] = 0
#         else:
#             visited[i] = 1
#             dfs(i + 2, ssum + sticker[i])
#             visited[i] = 0
#         if i + 1 < l:
#             visited[i + 1] = 1
#             dfs(i + 3, ssum + sticker[i + 1])
#             visited[i + 1] = 0
#         return
#     answer = 0
#     visited = [0] * l
#     dfs(0, 0)
#     return answer