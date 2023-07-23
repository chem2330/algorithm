def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x : (x[col - 1], -x[0]))
    # print(data)
    for i in data[row_begin - 1]:
        answer += i % row_begin
    # print(answer)
    for i in range(row_begin, row_end):
        tmp = 0
        for j in data[i]:
            tmp += j % (i + 1)
        answer = answer ^ tmp
        
    return answer