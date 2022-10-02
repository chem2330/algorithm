import heapq


def solution(n, costs):
    answer = 0
    visited = [0] * n
    arr = [[] for _ in range(n)]
    min_cost = 9999999999999999
    min_cost_node = []
    for cost in costs:
        a, b, c = cost
        arr[a].append([c, b])
        arr[b].append([c, a])
        if c < min_cost:
            min_cost = c
            min_cost_node = [a, b]
    answer += min_cost
    visited[min_cost_node[0]] = 1
    visited[min_cost_node[1]] = 1
    
    h = []
    for edge in arr[min_cost_node[0]]:
        if visited[edge[1]] == 0:
            heapq.heappush(h, edge)
    for edge in arr[min_cost_node[1]]:
        if visited[edge[1]] == 0:
            heapq.heappush(h, edge)
    
    while 1:
        while 1:
            v = heapq.heappop(h)
            if visited[v[1]] == 0:
                answer += v[0]
                visited[v[1]] = 1
                break
        if sum(visited) == n:
            break
        for edge in arr[v[1]]:
            if visited[edge[1]] == 0:
                heapq.heappush(h, edge)
    
    return answer