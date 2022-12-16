T = int(input())
for _ in range(T):
    N, M = map(int, input().split())  # 문서의 개수, 확인할 문서
    arr = list(map(int, input().split()))
    answer = 0
    while True:
        if arr[0] == max(arr):
            arr.pop(0)
            answer += 1
            if M == 0:
                break
            M -= 1
        else:
            tmp = arr.pop(0)
            arr.append(tmp)
            if M != 0:
                M -= 1
            else:
                M = len(arr) - 1
    print(answer)