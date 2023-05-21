from itertools import combinations


def solution(relation):
    n = len(relation[0])
    answer = 0
    answer_lst = []
    
    for i in range(1, n + 1):
        combs = combinations(range(n), i)
        # print(list(combs))
        for com in combs:
            tmp_lst = set()
            for j in range(len(relation)):
                tmp = ""
                for c in com:
                    tmp += relation[j][c]
                tmp_lst.add(tmp)
            if len(tmp_lst) == len(relation):
                flag = 0
                for tmp2 in answer_lst:
                    if not flag and set(tmp2) == set(tmp2).intersection(set(com)):
                        flag = 1
                if not flag:
                    answer_lst.append(com)
    
    
    # print(answer_lst)
    return len(answer_lst)