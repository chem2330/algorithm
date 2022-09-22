def solution(n, edge):
    arr = [[] for _ in range(n + 1)]
    for i in edge:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
    ans = [50001] * (n + 1)
    ans[0] = ans[1] = 0
    stack = [(1, 0)]
    while stack:
        v, cnt = stack.pop()
        for i in arr[v]:
            if cnt + 1 < ans[i]:
                ans[i] = cnt + 1
                stack.append((i, cnt + 1))
    return ans.count(max(ans))