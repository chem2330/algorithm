import heapq

def solution(operations):
    h = []
    for operation in operations:
        if operation == 'D 1':
            if h:
                h.remove(max(h))
        elif operation == 'D -1':
            if h:
                heapq.heappop(h)
        else:
            heapq.heappush(h, int(operation[2:]))
        print(h)
    if h:
        answer = [max(h), min(h)]
    else:
        answer = [0, 0]
    return answer