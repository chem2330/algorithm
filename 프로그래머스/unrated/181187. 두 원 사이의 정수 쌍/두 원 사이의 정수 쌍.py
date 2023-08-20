def solution(r1, r2):
    answer = 0
    for i in range(1, r2 + 1):
        # print((r2 * r2 - i * i) ** 0.5, max(0, r1 * r1 - i * i) ** 0.5)
        answer += int((r2 * r2 - i * i) ** 0.5) - int(max(0, r1 * r1 - i * i - 1) ** 0.5)
    answer += (r2 - r1 + 1)
    answer *= 4
    return answer
    # for i in range(1, r2 + 1):
    #     for j in range(1, r2 + 1):
    #         if r1 * r1 <= i * i + j * j <= r2 * r2:
    #             answer += 1
    # answer += (r2 - r1 + 1)
    # answer *= 4
    # return answer