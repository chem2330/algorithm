import heapq


def solution(jobs):
    answer = 0
    jobs_cnt = len(jobs)
    jobs.sort()
    time = 0
    h = []
    while 1:
        for i, job in enumerate(jobs):
            if job[0] > time:
                jobs = jobs[i:]
                break
            heapq.heappush(h, [job[1], job[0]])
            if i == len(jobs) - 1:
                jobs = []
        if h:
            v = heapq.heappop(h)
            answer += (time + v[0]) - v[1]
            time = time + v[0]
        elif jobs:
            time = jobs[0][0]
        else:
            break
            
    
    return answer // jobs_cnt