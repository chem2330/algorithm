import math

def solution(n, stations, w):
    answer = 0
    stations = sorted(stations)
    for i in range(len(stations) - 1):
        answer += math.ceil((stations[i + 1] - stations[i] - 1 - 2 * w) / (2 * w + 1))
    if stations[0] - 1 - w > 0:
        # print(stations[0] - 1 - w)
        answer += math.ceil((stations[0] - 1 - w) / (2 * w + 1))
    if n - stations[-1] - w > 0:
        # print(n - stations[-1] - w)
        answer += math.ceil((n - stations[-1] - w) / (2 * w + 1))

    return answer


# 시간초과
# def solution(n, stations, w):
#     answer = 0
#     lst = [0] * (n + 1)
#     for i in stations:
#         for j in range(-w, w + 1):
#             if 0 < i + j <= n:
#                 lst[i + j] = 1
#     idx = 1
#     while True:
#         if idx == n + 1:
#             break
#         if not lst[idx]:
#             answer += 1
#             idx = min(idx + 2 * w + 1, n + 1)
#         else:
#             idx += 1

#     return answer