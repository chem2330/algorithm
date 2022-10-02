def solution(tickets):
    answer_list = []
    airport = {}
    for ticket in tickets:
        if airport.get(ticket[0]):
            airport[ticket[0]] += [ticket[1]]
        else:
            airport[ticket[0]] = [ticket[1]]

    def dfs(lst):
        nonlocal visited
        if len(lst) == len(tickets) + 1:
            answer_list.append(lst)
            return
        v = lst[-1]
        if airport.get(v):
            for j in airport[v]:
                tmp2 = [v, j]
                tmp_lst = list(filter(lambda x: tickets[x] == tmp2, range(len(tickets))))
                for k in tmp_lst:
                    if visited[k] == 0:
                        visited[k] = 1
                        dfs(lst + [j])
                        visited[k] = 0
                        break

    visited = [0] * len(tickets)
    dfs(["ICN"])
    
    answer_list.sort()
    return answer_list[0]