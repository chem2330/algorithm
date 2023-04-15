def solution(number, k):
    answer = [number[0]]
    for i in range(1, len(number)):
        if k and answer[-1] < number[i]:
            while answer[-1] < number[i]:
                k -= 1
                answer.pop(-1)
                if not k or not answer:
                    break
            answer.append(number[i])
        else:
            answer.append(number[i])  
    return ''.join(answer[:len(number)-k])