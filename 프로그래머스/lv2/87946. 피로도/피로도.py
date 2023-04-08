import itertools


def solution(k, dungeons):
    answer = -1
    coms = itertools.permutations(range(len(dungeons)), len(dungeons))
    for com in coms:
        hp = k
        n = 0
        for i in com:
            if dungeons[i][0] <= hp:
                n += 1
                hp -= dungeons[i][-1]
            answer = max(answer, n)
    return answer