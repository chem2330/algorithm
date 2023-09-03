from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = {}
    
    for i in info:
        tmp = i.split()
        choose = tmp[:-1]  # 점수 제외
        score = int(tmp[-1])  # 점수
        
        for j in range(5):
            for c in list(combinations(choose, j)):
                tmp = ''.join(c)
                if tmp in info_dict:  # 점수제외 : 점수 형식으로 딕셔너리 저장
                    info_dict[tmp].append(score)
                else:
                    info_dict[tmp] = [score]
    
    for value in info_dict.values():  # 점수 기준으로 오름차순
        value.sort()
    
    for q in query:
        qry = q.split()
        qry_choose = qry[:-1]
        qry_score = int(qry[-1])
        
        while 'and' in qry_choose:  # and 제거
            qry_choose.remove('and')
        while '-' in qry_choose:  # - 제거
            qry_choose.remove('-')
        qry_choose = ''.join(qry_choose) 
        
        if qry_choose in info_dict:
            data = info_dict[qry_choose]  # 조건일때 점수들 찾기
            if len(data) > 0:  # 이분 탐색
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)
        else:  # 없는 경우 0
            answer.append(0)

    return answer