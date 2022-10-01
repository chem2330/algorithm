import heapq

def solution(n, works):
    answer = 0
    h = []
    for work in works:
        heapq.heappush(h, -work)
    while n:
        work = heapq.heappop(h)
        if work == 0:
            break
        heapq.heappush(h, work + 1)
        n -= 1
        
    for work in h:
        answer += work ** 2
    return answer