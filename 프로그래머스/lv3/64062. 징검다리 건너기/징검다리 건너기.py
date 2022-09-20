def solution(stones, k):
    answer = 0
    left = 1  # stone의 최솟값
    right = max(stones)
    
    while left <= right:  # 이진 탐색
        mid = (right + left) // 2  # 건널 수 있는 사람 수를 이진 탐색
        jump = 0
        for stone in stones:
            if stone - mid > 0:  # mid명이 지나갔을 때 stone이 남아 있음 -> 건널 수 있음
                jump = 0
            else:  # stone이 남아있지 않음 -> jump 해야함
                jump += 1

            if jump >= k:  # jump를 k가 넘으면 바로 break
                answer = mid  # 건널 수 있는 사람 수가 mid이니깐 answer 갱신
                right = mid - 1  # 건널 수 있는 사람 수를 낮춰보고 다시 while문 돌도록 함
                break

        else:  # 모두가 건널 수 있는 상황이므로 건널 수 있는 사람의 수를 높여보고 다시 while문 돌도록 함
            left = mid + 1
            
    return answer