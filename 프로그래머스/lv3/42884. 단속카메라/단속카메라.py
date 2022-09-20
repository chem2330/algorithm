def solution(routes):
    answer = []
    routes.sort(key=lambda x:x[1])
    for route in routes:
        if answer:
            if answer[-1] < route[0]:
                answer.append(route[1])
                
        else:
            answer.append(route[1])
            
    # arr = [[] for _ in range(60001)]
    # routes.sort(key=lambda x:x[1])
    # for i, route in enumerate(routes):
    #     for j in range(route[0], route[1] + 1):
    #         arr[j + 30000].append(i)
    # for i, route in enumerate(routes):
    #     max_
        
    
    return len(answer)