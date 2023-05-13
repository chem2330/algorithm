def solution(numbers):
    answer = []
    for num in numbers:
        bi = list(map(int, bin(num)[2:]))
        if len(bi) == sum(bi):
            tmp = [1, 0] + [1] * (len(bi) - 1)
        else:
            tmp = bi
            for i in range(len(bi)-1, -1, -1):
                if bi[i] == 0:
                    tmp[i] = 1
                    if i != len(bi) - 1:
                        tmp[i + 1] = 0
                    break
        answer.append(int(''.join(map(str, tmp)), 2))
    return answer