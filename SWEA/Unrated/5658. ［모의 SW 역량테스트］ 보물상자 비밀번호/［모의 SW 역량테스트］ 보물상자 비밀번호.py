T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 총 수, K번째로 큰 수 출력
    arr = list(input())
    arr = arr * 2
    lst = set()
    for i in range(N):
        lst.add(int(''.join(arr[i:i+(N//4)]), 16))
    lst = sorted(lst, reverse=True)
    print(f'#{tc} {lst[K - 1]}')