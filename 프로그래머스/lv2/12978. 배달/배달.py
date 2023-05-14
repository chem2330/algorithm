def solution(N, road, K):
    answer = 0
    arr = [[1000000] * (N + 1) for _ in range(N + 1)]
    for a, b, c in road:
        if arr[a][b] > c:
            arr[a][b] = c
            arr[b][a] = c
    lst = [1000000] * (N + 1)
    lst[1] = 0
    stack = [1]
    while stack:
        s = stack.pop()
        for i in range(1, N + 1):
            if lst[i] > lst[s] + arr[s][i]:
                stack.append(i)
                lst[i] = lst[s] + arr[s][i] 
    print(lst)
    for i in lst:
        if i <= K:
            answer += 1
    return answer