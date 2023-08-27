def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        # 1일때는 예외처리
        if i == 1:
            answer.append(0)
            continue
        
        lst = [1]  # 가능한 약수 리스트
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0 and j <= 10000000:  # 10,000,000까지의 숫자가 적힌 블록들을 이용
                lst.append(j)
            if i % j == 0 and i // j <= 10000000:
                lst.append(i // j)
        answer.append(max(lst))  # 최댓값 추가
    return answer