N, S = map(int, input().split())  # 개수, 부분합
arr = list(map(int, input().split()))

if sum(arr) < S:
    print(0)

else:
    ssum = arr[0]
    start = 0
    end = -1
    ans = N
    while True:
        if ssum >= S:
            if (start - end) < ans:
                ans = start - end
            end += 1
            ssum -= arr[end]
        elif start < N - 1:
            start += 1
            ssum += arr[start]
        else:
            break
    print(ans)