M = int(input())  # 컵 위치 변경 횟수
ball = 1
for _ in range(M):
    a, b = map(int, input().split())  # 바꾸는 컵의 숫자
    if a == ball:
        ball = b
    elif b == ball:
        ball = a
print(ball)