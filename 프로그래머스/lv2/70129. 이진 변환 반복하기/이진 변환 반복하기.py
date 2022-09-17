def solution(s):
    cnt_zero = 0
    cnt_while = 0
    while s != '1':
        cnt_zero += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt_while += 1
    answer = [cnt_while, cnt_zero]
    return answer